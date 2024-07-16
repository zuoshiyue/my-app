from models import Account, Bill
from utils import load_data, save_data
import json
from pathlib import Path

class App:
    def __init__(self):
        self.accounts = load_data('data/accounts.json') or []
        self.bills = load_data('data/bills.json') or []

    def add_account(self, account):
        self.accounts.append(account)
        save_data(self.accounts, 'data/accounts.json')

    def load_data(self, filename):
        # 假设 load_data 方法已经实现并可以从文件中加载数据
        pass

    def save_data(self, data, filename):
        # 将数据保存到 JSON 文件
        file_path = Path(filename)
        with open(file_path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def remove_account(self, account_name):
        self.accounts = [acc for acc in self.accounts if acc.name != account_name]
        save_data(self.accounts, 'data/accounts.json')

    def add_bill(self, bill):
        self.bills.append(bill)
        save_data(self.bills, 'data/bills.json')

    def remove_bill(self, bill_id):
        self.bills = [bill for bill in self.bills if bill['id'] != bill_id]
        save_data(self.bills, 'data/bills.json')
