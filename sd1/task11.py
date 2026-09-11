import pytest

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, inc):
        if inc > 0:
            return BankAccount(self.balance + inc)
        return self

    def withdraw(self, dec):
        if dec > 0 and self.balance - dec >= 0:
            return BankAccount(self.balance - dec)
        return self

    def getBalance(self):
        return self.balance


def test_bank_account():
    account = BankAccount(10)
    account = account.deposit(20)
    account = account.withdraw(30)
    assert 0 == account.getBalance()

    account2 = BankAccount(10)
    account2 = account2.withdraw(20)
    assert 10 == account2.getBalance()

    account2 = account2.deposit(-10)
    assert 10 == account2.getBalance()

    account2 = account2.withdraw(-10)
    assert 10 == account2.getBalance()




