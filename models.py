from enum import Enum

class AccountLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Server(Enum):
    SERVER_A = "Server A"
    SERVER_B = "Server B"
    # ... 其他服务器

class Sect(Enum):
    SECT_X = "Sect X"
    SECT_Y = "Sect Y"
    # ... 其他门派

class Technique(Enum):
    TECHNIQUE_1 = "Technique 1"
    TECHNIQUE_2 = "Technique 2"
    # ... 其他心法

class Account:
    def __init__(self, name, level, server, sect, technique, username, password):
        self.name = name
        self.level = level
        self.server = server
        self.sect = sect
        self.technique = technique
        self.username = username
        self.password = password

class Bill:
    def __init__(self, date, character_name, instance_name, expenditure, income, net_income):
        self.id = id  # Assuming 'id' is a unique identifier for the bill
        self.date = date
        self.character_name = character_name
        self.instance_name = instance_name
        self.expenditure = expenditure
        self.income = income
        self.net_income = net_income
