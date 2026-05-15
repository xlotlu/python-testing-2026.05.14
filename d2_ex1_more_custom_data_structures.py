# Using the TDD approach (test-driven development):
#
#
# 1) write a `raise_salary(percentage)` method,
#    where percentage must be one of the admitted values,
#    namely: 5, 10, 15, 20.
#    
#
# 2) write a `pay_salary()` method, that has no arguments,
#    which deposits the employee's salary into their bank account.



from d1_ex3_testing_custom_data_structures import BankAccount

class Employee:
    RAISE_PERCENTAGES = (5, 10, 15, 20)

    def __init__(self, name: str, bank_account: BankAccount, salary: int):
        self.name = name
        self.bank_account = bank_account
        self.salary = salary

    def raise_salary(self, percentage):
        if percentage not in self.RAISE_PERCENTAGES:
            raise ValueError("Invalid raise percentage: %s" % percentage)

        self.salary += self.salary * percentage / 100

    def pay_salary(self):
        self.bank_account.deposit(self.salary)