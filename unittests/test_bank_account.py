import unittest

from d1_ex3_testing_custom_data_structures import (
    BankAccount,
    InsufficientFundsException,
)

class TestBankAccountCreation(unittest.TestCase):
    def test_account_creation_with_zero_balance(self):
        account = BankAccount()
        self.assertEqual(account.balance, 0)

    def test_account_creation_with_positive_balance(self):
        account = BankAccount(100)
        self.assertEqual(account.balance, 100)


class TestBankAccountOperations(unittest.TestCase):

    #@classmethod
    #def setUpClass(cls):
    #    # this will be persistent across all tests
    #    cls.ba = BankAccount(20)
        

    # acesta este un "fixture".
    # se rulează pentru fiecare test.
    def setUp(self):
        self.account = BankAccount(100)

    def tearDown(self):
        pass

    def test_deposit(self):
        self.account.deposit(40)
        self.assertEqual(self.account.balance, 140)

    def test_withdrawal(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.balance, 60)

    def test_withdrawal_higher_than_balance(self):
        with self.assertRaises(InsufficientFundsException):
            self.account.withdraw(101)
        self.assertEqual(self.account.balance, 100)

    def test_operation_with_amount_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

        with self.assertRaises(ValueError):
            self.account.withdraw(0)

        self.assertEqual(self.account.balance, 100)

    def test_multiple_operations(self):
        self.account.deposit(100)   # 200
        self.account.withdraw(20)   # 180
        self.account.deposit(50)    # 230
        self.account.withdraw(30)   # 200
        self.assertEqual(self.account.balance, 200)