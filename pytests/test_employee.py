import pytest

from d2_ex1_more_custom_data_structures import Employee
from d1_ex3_testing_custom_data_structures import BankAccount


@pytest.fixture
def account100():
    return BankAccount(100)

def test_employee_creation(account100):
    name = "Robert"
    salary = 50
    employee = Employee(name, account100, salary)

    assert account100 == employee.bank_account
    assert name == employee.name
    assert salary == employee.salary

def test_employee_raise(account100):
    salary = 100

    employee = Employee("test name", account100, salary)

    employee.raise_salary(5)

    assert employee.salary == 105

def test_wrong_raise_percentage(account100):
    salary = 100

    employee = Employee("test name", account100, salary)
    
    # an invalid raise percentage should be denied
    with pytest.raises(ValueError):
        employee.raise_salary(7)

    # we should also make sure that an invalid raise percentage
    # results in no change in salary
    assert salary == employee.salary