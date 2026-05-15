import pytest

from d1_ex3_testing_custom_data_structures import (
    BankAccount,
    InsufficientFundsException,
)

def test_account_creation_with_zero_balance():
    account = BankAccount()
    assert account.balance == 0

def test_account_creation_with_positive_balance():
    account = BankAccount(100)
    assert account.balance == 100

@pytest.fixture
def account():
    return BankAccount(100)

def test_deposit(account):
    account.deposit(40)
    assert account.balance == 140

def test_withdrawal(account):
    account.withdraw(40)
    assert account.balance == 60

def test_operation_with_amount_zero(account):
    with pytest.raises(ValueError):
        account.deposit(0)

    with pytest.raises(ValueError):
        account.withdraw(0)

    assert account.balance == 100

def test_withdrawal_higher_than_balance(account):
    with pytest.raises(InsufficientFundsException):
        account.withdraw(101)
    assert account.balance == 100

def test_multiple_operations(account):
    account.deposit(100)   # 200
    account.withdraw(20)   # 180
    account.deposit(50)    # 230
    account.withdraw(30)   # 200
    assert account.balance == 200