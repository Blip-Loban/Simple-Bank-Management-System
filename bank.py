class Bank:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.total_bank_balance=100000
        self.user_accounts=[]
        self.isGivingLoan=True
        self.total_loan_given=0
    def admin_login(self,username,password):
        if username=='admin' and password ==1234:
            return True
        else:
            return False
    def add_user(self,user):
        self.user_accounts.append(user)
    def view_all_user(self):
        for i in self.user_accounts:
            print(i)
    def check_total_bank_balance(self):
        print(f"Total Banks Money: {self.total_bank_balance}")
    def bank_decrease(self,money):
        self.total_bank_balance-=money
    def bank_increase(self,money):
        self.total_bank_balance+=money
    
    def change_loan_status(self,bool):
        self.isGivingLoan=bool
    
    def delete_user(self):
        self.user_accounts.pop()
