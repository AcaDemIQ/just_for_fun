import pytest

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, inc):
        self.balance += inc

    def withdraw(self, dec):
        self.balance -= dec

    def getBalance(self):
        return self.balance


def test_bank_account():
    account = BankAccount(10)
    account.deposit(20)
    account.withdraw(30)
    assert 0 == account.getBalance()




