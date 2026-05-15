import pytest

from d1_ex3_testing_custom_data_structures import (
    BankAccount,
    InsufficientFundsException,
)

from d2_ex1_more_custom_data_structures import Employee


def create_account(balance):
    return BankAccount(balance)


@pytest.fixture
def account0():
    return BankAccount(0)

@pytest.fixture
def employee100(account0):
    return Employee("test name", account0, 100)

def test_pay_salary(employee100):
    employee100.pay_salary()

    assert employee100.bank_account.balance == employee100.salary

    employee100.pay_salary()
    assert employee100.bank_account.balance == employee100.salary * 2

def test_withdraw_before_payment(employee100):
    with pytest.raises(InsufficientFundsException):
        employee100.bank_account.withdraw(100)

def test_withdraw_after_payment(employee100):
    initial_balance = employee100.bank_account.balance

    employee100.pay_salary()
    amount = employee100.salary
    employee100.bank_account.withdraw(amount)

    assert employee100.bank_account.balance == initial_balance

def test_repeated_payments_and_withdrawals(employee100):
    emp = employee100
    account = emp.bank_account
    salary = emp.salary

    emp.pay_salary()
    assert account.balance == salary
    
    account.withdraw(50)
    emp.pay_salary()
    assert account.balance == salary * 2 - 50


