import random
import datetime
class User:

    def __init__(self,name,email,address,account_type) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.account_number=random.randint(1,10)
        self.__balance=0
        self.transaction_history=[]
        self.loan_remaining=2
    def deposite(self,money):
        self.__balance+=money
        date=datetime.datetime.now()
        self.transaction_history.append(f'Deposited amount: {money} time: {date}')
    def withdrawl(self,money):
        if money > self.__balance:
            print("Bankrupt!!")
        else:
            self.__balance-=money
            date=datetime.datetime.now()
            self.transaction_history.append(f'Withdrawed amount: {money} time: {date}')
    def check_balance(self):
        print(f'Your Current Balance {self.__balance}') 
    def check_transaction_history(self):
        for history in self.transaction_history:
            print(history)
    def take_loan(self,money,bank):
        if self.loan_remaining>0 and bank.isGivingLoan==True:
            self.__balance+=money
            self.loan_remaining-=1
        else:
            print(f'You Can not Take Loans. Loan attempts remaining {self.loan_remaining}')

    def transfer_money(self,id,money,all_user):
        if money <self.__balance:
            if id in all_user.account_number:
                self.__balance-=money
                all_user.__balance+=money
            else:
                print("Invalid Account Name")
        else:
            print('Bankrupt!!')
    


    def __repr__(self) -> str:
        print(f"{self.name} {self.account_type} {self.account_number} {self.address} {self.email}")
    