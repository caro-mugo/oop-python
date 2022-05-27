
class Bank: 
    
    def __init__(self,account_name,account_number,bank_name,account_balance,pin):
        self.account_name=account_name
        self.account_number=account_number
        self.account_balance=account_balance
        self.pin=pin
        self.bank_name=bank_name
        
        
    def deposit(self):
            amount=int(input("Enter amount"))
            amount+=self.account_balance
            return amount
            
        
    def withdraw(self):
            amount=int(input("Enter amount"))
            self.account_balance-=amount
            return self.account_balance
            
            
            
        
        
                                         
        
        