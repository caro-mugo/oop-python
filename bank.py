# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.
class Bank: 
    
    def __init__(self,account_name,account_number):
        self.account_name=account_name
        self.account_number=account_number
        # self.account_balance=account_balance
        # self.pin=pin
        # self.bank_name=bank_name
        self.account_balance=0
        self.deposits=[]
        self.withdrawals=[]

        
        
    # def deposit(self):
    #         amount=int(input("Enter amount"))
    #         amount+=self.account_balance
    #         return f"                                                                                                                                                                                                                                                                                                                                                                                                                                           Hello{self.account_name} you have deposited {self.amount}and your balance is{self.account_balance}"
            
        
    # def withdraw(self,):
    #         amount=int(input("Enter amount"))
    #         self.account_balance-=amount
    #         return self.account_balance
            
            
    def deposit(self,amount):
        
        if amount<=0:
            return f"deposit must be positive amount"
        else:
            self.account_balance+=amount 
            self.deposits.append(amount)
            return f"Hello {self.account_name} you have deposited{amount} and your account balance is {self.account_balance}"
    def withdraw(self,amount): 
        self.transact=100
        if amount <=0:
            return f"withdraw should be greater than zero"  
        elif amount>self.account_balance:
            return f"your balance is {self.account_balance},you can't withdraw {amount}"
        else:
            self.account_balance-=amount+self.transact
            self.withdrawals.append(amount)

            return f"Hello {self.account_name} you have withdrawn{amount} your new balance is {self.account_balance}"
               
    def deposits_statement(self):
        for y in self.deposits:
            print(y,end="\n")

        

    def withdrawals_statement(self):
        for i in self.withdrawals:
            print(y,end="\n")
    def balance(self):
        return f"{self.account_balance}"
            
            

        

            
        
        
                                         
        
        