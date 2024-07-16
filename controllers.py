from app import App
from models import Account, Bill


class Controller:
    def __init__(self):
        self.app = App()

    def add_account(self, account_data):
        account = Account(**account_data)
        self.app.add_account(account)

    def remove_account(self, account_name):
        self.app.remove_account(account_name)

    def edit_account(self, account_data, account_name):
        # 在 accounts 列表中找到匹配的账户名
        for i, account in enumerate(self.app.accounts):
            if account.name == account_name:
                # 更新账户信息
                self.app.accounts[i] = Account(**account_data)
                break
        # 保存更新后的账户信息到文件
        self.app.save_data(self.app.accounts, 'data/accounts.json')

    def add_bill(self, bill_data):
        bill = Bill(**bill_data)
        self.app.add_bill(bill)

    def remove_bill(self, bill_id):
        self.app.remove_bill(bill_id)

    def get_accounts(self):
        # 使用 App 类的 accounts 属性获取账户列表
        return self.app.accounts
