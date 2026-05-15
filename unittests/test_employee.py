import unittest

from d2_ex1_more_custom_data_structures import Employee
from d1_ex3_testing_custom_data_structures import BankAccount


class CheckEmployeeTest(unittest.TestCase):
    @staticmethod
    def create_account(balance=100):
        return BankAccount(balance)

    def test_employee_creation(self):
        name = "Robert"
        account = self.create_account()
        salary = 50
        
        employee = Employee(name, account, salary)

        self.assertEqual(account, employee.bank_account)
        self.assertEqual(name, employee.name)
        self.assertEqual(salary, employee.salary)
        
    def test_employee_raise(self):
        salary = 100
        account = self.create_account()
        employee = Employee("test name", account, salary)

        employee.raise_salary(5)

        self.assertEqual(employee.salary, 105)

    def test_wrong_raise_percentage(self):
        salary = 100
        account = self.create_account()
        employee = Employee("test name", account, salary)
        
        # an invalid raise percentage should be denied
        with self.assertRaises(ValueError):
            employee.raise_salary(7)

        # we should also make sure that an invalid raise percentage
        # results in no change in salary
        self.assertEqual(salary, employee.salary)
