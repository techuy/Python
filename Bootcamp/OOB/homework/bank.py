class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,money):
        self.balance+=money
        return "Deposit Accepted"

    def withdraw(self,withdrawal):
        if withdrawal<=self.balance:
            self.balance-=withdrawal
            return "Withdrawal Accepted" 
        else:
            return "Funds Unavailable"
        

    def __str__(self):
        return (f"Account Owner: {self.owner} \nAccount Balance: {self.balance}")

acc1 = Account("Jose",100)
print(acc1)
print(acc1.owner)
print(acc1.balance)
print(acc1.deposit(50))
print(acc1.withdraw(500))