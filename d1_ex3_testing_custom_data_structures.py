# Write tests using unittest for
# BankAccount.deposit() and
# BankAccount.withdraw()


class InsufficientFundsException(Exception):
    pass


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('value should be greater than 0')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('value should be greater than 0')
        if amount > self.balance:
            raise InsufficientFundsException('insufficient funds')
        self.balance -= amount


# we want to test the following...

# test_account_creation_with_zero_balance

# test_account_creation_with_positive_balance


# test_deposit

# test_withdrawal

# test_withdrawal_higher_than_balance


# test_operations_with_zero_amount
# test_operations_with_negative_amount

# test_multiple_operations
