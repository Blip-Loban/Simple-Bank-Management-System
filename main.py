from user import User
from bank import Bank

myBank=Bank('Loban','Gulshan')
print('1.User Login')
print('2.Admin Login')
a=int(input())

if a==1:
    while(True):

        print("1.Create Account")
        print("2.Deposite")
        print("3.Withdraw")
        print("4.Check Balance")
        print("5.Take Loan")
        print("6.Transfer Money")
        print("7.Exist")
        b=int(input())

        if b==1:
            u1=User('monju',"asd","sda",'saving')
            myBank.add_user(u1)
            
        
        elif b==2:
            print("Enter amount:")
            tmp=int(input())
            u1.deposite(tmp)
            myBank.bank_increase(tmp)
        elif b==3:
            print("Enter amount:")
            tmp=int(input())
            u1.withdrawl(tmp)
            myBank.bank_decrease(tmp)
        elif b==4:
            u1.check_balance()
        elif b==5:
            print("Enter amount:")
            tmp=int(input())
            u1.take_loan(tmp,myBank)
            myBank.bank_decrease(tmp)
        elif b==6:
            u1.transfer_money(2,100,myBank.user_accounts)
        elif b==7:
            break
            

elif a==2:
    print("UserName:")
    tmp1=input()       
    print("Password:")
    tmp2=int(input())
    admin=myBank.admin_login(tmp1,tmp2)
    if admin==True:
        while True:
            print("1.Create Account")
            print("2.Delete User")
            print("3.See All User")
            print("4.Check Bank Total Balance")
            print("5.Total Loan Amount")
            print("6.Change Loan Feature")
            print("7.Exist")
            b=int(input())

            if b==1:
                u1=User('monju',"asd","sda",'saving')
                myBank.add_user(u1)
                
            
            elif b==2:
               myBank.delete_user()
            elif b==3:
               myBank.view_all_user()
            elif b==4:
               myBank.total_bank_balance()
            elif b==5:
               myBank.total_loan_given()
            elif b==6:
                abs=bool(input())
                myBank.change_loan_status(abs)
            elif b==7:
                break

    else:
        print('Incorrect Login Info')

        
        