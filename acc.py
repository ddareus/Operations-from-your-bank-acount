from tabnanny import check


class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r', encoding="utf8") as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w', encoding="utf8") as file:
            file.write(str(self.balance))

# account = Account("balance.txt")
# print(account.balance)
# # account.deposit(200)
# account.withdraw(50)
# print(account.balance)
# account.commit()

# Inheritance

class Checking(Account):
    """ This class generates checking account objects"""
    
    type = "checking"
    
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
        
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        
Peda_checking = Checking("peda.txt", 10)
Peda_checking.transfer(100)
print(Peda_checking.balance)
Peda_checking.commit()
print(Peda_checking.type)

Tanounou_checking = Checking("tanounou.txt", 10)
Tanounou_checking.transfer(100)
print(Tanounou_checking.balance)
Tanounou_checking.commit()
print(Tanounou_checking.type)

print(Tanounou_checking.__doc__)
