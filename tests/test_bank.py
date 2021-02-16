"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank, Account
from datetime import datetime


@pytest.fixture
def bank() -> Bank:
    return Bank()


def test_accounts_are_immutable():
    account = Account('Immutable')
    with pytest.raises(Exception):
        # This operation should raise an exception
        account.name = 'Mutable'


def test_bank_creates_empty(bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0


def test_can_create_and_get_account(bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'


def test_cannot_duplicate_accounts(bank):
    bank.create_account('duplicate')
    bank.create_account('duplicate')

    assert len(bank.accounts) == 1


def test_cannot_modify_accounts_set(bank):
    accounts = bank.accounts
    accounts.add(Account('New Account'))

    assert len(bank.accounts) == 0


# TODO: Add unit tests for bank.add_funds()

def test_add_funds(bank):
    name ="Test"
    amount = 5
    date_string = '21 June, 2018'
    now = datetime.strptime(date_string, "%d %B, %Y")

    bank.create_account('Test')
    bank.add_funds(name, amount, now)

    assert len(bank.transactions) == 1

    transaction_list=list(bank.transactions)

    assert transaction_list[0].account.name == name
    assert transaction_list[0].date == now
    assert transaction_list[0].amount == amount