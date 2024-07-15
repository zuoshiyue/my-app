import sys
from PyQt5.QtWidgets import (QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QListWidget, QLineEdit, QMessageBox, QInputDialog, QDialog,
                             QFormLayout, QLabel, QTextEdit, QApplication, QComboBox, QDialogButtonBox, QDateEdit)
from PyQt5.QtCore import Qt
from models import Account, AccountLevel, Server, Sect, Technique
from controllers import Controller
from datetime import date

class AccountDialog(QDialog):
    def __init__(self, controller, account=None, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.account = account
        self.init_ui()

    def init_ui(self):
        self.layout = QFormLayout()
        self.name_edit = QLineEdit()
        self.level_combo = QComboBox()
        self.level_combo.addItems([lvl.name for lvl in AccountLevel])
        self.server_combo = QComboBox()
        self.server_combo.addItems([srv.value for srv in Server])
        self.sect_combo = QComboBox()
        self.sect_combo.addItems([sect.value for sect in Sect])
        self.technique_combo = QComboBox()
        self.technique_combo.addItems([tech.value for tech in Technique])
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.layout.addRow("名称", self.name_edit)
        self.layout.addRow("等级", self.level_combo)
        self.layout.addRow("区服", self.server_combo)
        self.layout.addRow("门派", self.sect_combo)
        self.layout.addRow("心法", self.technique_combo)
        self.layout.addRow("账号", self.username_edit)
        self.layout.addRow("密码", self.password_edit)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)

        if self.account:
            self.name_edit.setText(self.account.name)
            self.level_combo.setCurrentText(self.account.level.name)
            self.server_combo.setCurrentText(self.account.server.value)
            self.sect_combo.setCurrentText(self.account.sect.value)
            self.technique_combo.setCurrentText(self.account.technique.value)
            self.username_edit.setText(self.account.username)
            self.password_edit.setText(self.account.password)

    def get_account_data(self):
        return {
            "name": self.name_edit.text(),
            "level": self.level_combo.currentText(),
            "server": self.server_combo.currentText(),
            "sect": self.sect_combo.currentText(),
            "technique": self.technique_combo.currentText(),
            "username": self.username_edit.text(),
            "password": self.password_edit.text()
        }

class BillDialog(QDialog):
    def __init__(self, controller, bill=None, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.bill = bill
        self.init_ui()

    def init_ui(self):
        self.layout = QFormLayout()
        self.date_edit = QDateEdit(date.today())
        self.character_name_edit = QLineEdit()
        self.instance_name_edit = QLineEdit()
        self.expenditure_edit = QLineEdit()
        self.income_edit = QLineEdit()
        self.net_income_edit = QLineEdit()

        self.layout.addRow("日期", self.date_edit)
        self.layout.addRow("角色名称", self.character_name_edit)
        self.layout.addRow("副本名称", self.instance_name_edit)
        self.layout.addRow("支出", self.expenditure_edit)
        self.layout.addRow("收入", self.income_edit)
        self.layout.addRow("净收入", self.net_income_edit)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)

        if self.bill:
            self.date_edit.setDate(self.bill.date)
            self.character_name_edit.setText(self.bill.character_name)
            self.instance_name_edit.setText(self.bill.instance_name)
            self.expenditure_edit.setText(str(self.bill.expenditure))
            self.income_edit.setText(str(self.bill.income))
            self.net_income_edit.setText(str(self.bill.net_income))

    def get_bill_data(self):
        return {
            "date": self.date_edit.date().toString(Qt.ISODate),
            "character_name": self.character_name_edit.text(),
            "instance_name": self.instance_name_edit.text(),
            "expenditure": float(self.expenditure_edit.text()),
            "income": float(self.income_edit.text()),
            "net_income": float(self.net_income_edit.text())
        }

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.init_ui()

    def init_ui(self):
        self.tabs = QTabWidget()
        self.home_tab = QWidget()
        self.account_tab = QWidget()
        self.bill_tab = QWidget()
        self.tabs.addTab(self.home_tab, "首页")
        self.tabs.addTab(self.account_tab, "账户信息")
        self.tabs.addTab(self.bill_tab, "账单信息")
        self.setCentralWidget(self.tabs)

        # 首页内容
        self.welcome_label = QLabel("欢迎使用本应用程序")
        layout = QVBoxLayout()
        layout.addWidget(self.welcome_label)
        self.home_tab.setLayout(layout)

        # 账户信息页面
        self.account_list = QListWidget()
        self.account_add_button = QPushButton("添加账户")
        self.account_add_button.clicked.connect(self.add_account)
        self.account_remove_button = QPushButton("删除账户")
        self.account_remove_button.clicked.connect(self.remove_account)
        self.account_layout = QVBoxLayout()
        self.account_layout.addWidget(self.account_list)
        self.account_layout.addWidget(self.account_add_button)
        self.account_layout.addWidget(self.account_remove_button)
        self.account_tab.setLayout(self.account_layout)

        # 账单信息页面
        # 实现账单信息页面的UI布局
        # ...

        self.setWindowTitle("综合信息管理")
        self.resize(800, 600)

    def add_account(self):
        dialog = AccountDialog(self.controller)
        if dialog.exec_():
            account_data = dialog.get_account_data()
            self.controller.add_account(account_data)
            self.account_list.addItem(account_data["name"])

    def remove_account(self):
        current_item = self.account_list.currentItem()
        if current_item:
            name = current_item.text()
            _, ok = QInputDialog.getText(self, "确认删除", f"请输入账户名称 '{name}' 确认删除：",
                                         QLineEdit.Normal, name)
            if ok and name == current_item.text():
                self.controller.remove_account(name)
                self.account_list.takeItem(self.account_list.currentRow())

    # 其他方法，如编辑账户、添加账单等
    # ...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())