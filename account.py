from datetime import date

class Account:

    def __init__(self, account_nr):
        
        self.account_nr = account_nr
        self.account_balance = 0
        self.transaction_log = []

    def add_transaction(self, amount, transaction_type):
        """ adds transaction to account transaction log """
        transaction = dict()

        transaction["account_nr"] = self.account_nr
        transaction["amount"] = str(amount)
        transaction["type"] = transaction_type
        transaction["date"] = str(date.today())

        self.transaction_log.append(transaction)
    def get_account_balance(self):
        """ returns account balance"""
        return self.account_balance
    def get_transactions(self):
        """ returns list of transactions """
        return self.transaction_log
    def deposit(self, deposit):
        """ updates account balance with deposit """
        self.account_balance += deposit
    def withdraw(self, withdrawal_amount):
        """ updates account balance with withdrawal """
        self.account_balance -= withdrawal_amount
