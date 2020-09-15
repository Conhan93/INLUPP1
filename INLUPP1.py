from account import Account
import pickle
import os

class ATM:

    def __init__(self):

        # Declare list to store accounts
        self.accounts = []

        # Load accounts from file if available
        self.load_files()

        # transaction types
        self.type_withdrawal = "uttag"
        self.type_deposit = "ins"

    def main_menu(self):
        """ Runs main loop and display main menu """
        
        while True:
            self.print_main_menu()

            selection = input("Ange menyval>")

            if selection == "1":
                self.create_account()
            elif selection == "2":
                self.administer_account()
            elif selection == "3":
                break
            else:
                print("Felaktig inmatning. Prova igen")

        self.save_to_file()

    def print_main_menu(self):
        """ Prints main menu text """
        print("****HUVUDMENY****")
        print("1. Skapa Konto\n2. Administrera Konto\n3. Avsluta")
    def create_account(self):
        """ Handles account creation """
        while True:
            new_account_nr = input("Ange kontonummer>")
            # skips checking account numbers if account list is empty
            if self.accounts:
                if new_account_nr not in [account.account_nr for account in self.accounts]:
                    break
                else:
                    print("kontonummer redan taget, ange ett nytt")
        # Adds created account to ATM account list
        self.accounts.append(Account(new_account_nr))
    def administer_account(self):
        """ Handles login and account administration loop """

        # retrieves active account
        active_account = self.login()

        # Account administration loop
        while True:
            print("****KONTOMENY**** - konto:" + active_account.account_nr)
            selection = input("1. Ta ut pengar\n2. Sätt in pengar\n3. Visa Saldo\n4. Visa transaktioner\n5. Avsluta")
            if selection == "1":
                self.withdraw_from_account(active_account)
            elif selection == "2":
                self.deposit_to_account(active_account)
            elif selection == "3":
                print("Saldo: " + str(active_account.get_account_balance()))
            elif selection == "4":
                self.display_transactions(active_account)
            elif selection == "5":
                return
            else:
                print("Felaktig inmatning, prova igen")

    def login(self):
        """ Handles login to account, returns active account object"""
        while True:
            account_nr = input("Ange kontonummer")
            for account in self.accounts:
                if account_nr == account.account_nr:
                    return account
            print("hittade inget konto med det kontonummret")
    def deposit_to_account(self, active_account):
        """ Handles making deposition to account and updating transaction log"""
        while True:
            try:
                deposit_amount = float(input("Ange belopp>"))
                if deposit_amount > 0:
                    active_account.deposit(deposit_amount)
                    active_account.add_transaction(deposit_amount, self.type_deposit)
                    return
                else:
                    print("belopped måste vara större än 0")
            except:
                print("Felaktig inmatning, prova igen")
    def withdraw_from_account(self, active_account):
        """ Handles making withdrawals from account and updating transaction log"""
        while True:
            try:
                withdrawal_amount = float(input("Ange belopp>"))
                if withdrawal_amount <= active_account.account_balance:
                    active_account.withdraw(withdrawal_amount)
                    active_account.add_transaction(withdrawal_amount, self.type_withdrawal)
                    return
                else:
                    print("belopped får inte vara större än saldot på kontot")
            except:
                print("felaktig inmatning, prova igen")
    def display_transactions(self, active_account):
        """ Prints account transaction log """
        transaction_log = active_account.get_transactions()

        if transaction_log:
            print("****TRANSAKTIONER****")
            print("Konto\tBelopp\tTyp\tDatum")
            for transaction in transaction_log:
                print("\t".join(transaction.values()))
        else:
            print("det här kontot har inga transaktioner")

    def save_to_file(self):
        """ Saves accounts to file, creates file if one doesn't exist """
        
        with open("./accountfiles.pickle", "wb") as out:
            pickle.dump(self.accounts, out)

    def load_files(self):
        """ Loads accounts from file """
        try:
            with open("./accountfiles.pickle", "rb") as file_in:
                self.accounts = pickle.load(file_in)
        except:
            print("Hittade inga kontofiler")


if __name__ == '__main__':
    atm = ATM()
    atm.main_menu()