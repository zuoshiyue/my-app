from models import Account, Bill
from utils import load_data, save_data

class App:
    def __init__(self):
        self.accounts = load_data('data/accounts.json') or []
        self.bills = load_data('data/bills.json') or []

    def add_account(self, account):
        self.accounts.append(account)
        save_data(self.accounts, 'data/accounts.json')

    def remove_account(self, account_name):
        self.accounts = [acc for acc in self.accounts if acc['name'] != account_name]
        save_data(self.accounts, 'data/accounts.json')

    def add_bill(self, bill):
        self.bills.append(bill)
        save_data(self.bills, 'data/bills.json')

    def remove_bill(self, bill_id):
        self.bills = [bill for bill in self.bills if bill['id'] != bill_id]
        save_data(self.bills, 'data/bills.json')
