import pytest
from fixtures import BankAccount
@pytest.fixture
def fresh_account():
    account=BankAccount(100)
    return account
def test_deposit(fresh_account):
    fresh_account.deposit(50)
    fresh_account.withdraw(30)
    assert fresh_account.balance==120