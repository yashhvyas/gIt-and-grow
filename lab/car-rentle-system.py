class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    def deposit(self, amount):
            self.balance += amount
            print("deposited aumount =", amount)
            print("total balance",self.balance)
    def withdraw(self, amount):
            self.balance -= amount
            print("withdraw aumount =", amount)
            # print("total balance", self.balance)
            totalbalance = self.balance
            if self. balance <= totalbalance:
              print("insufficient balance")
    

            
            

# A1 = Account(1000, 1234567)
# print(A1.balance)
A2 = Account(10000, 9327620204)
print(A2.balance)
A2. deposit(5000)
A2. withdraw(16000)



