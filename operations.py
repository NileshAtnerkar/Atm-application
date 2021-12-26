import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="Nilesh@123", database="Atm")
s = con.cursor()

from exceptions import DepositError,WithdrawError,InsufficientError
bal=500.00
def deposit():
    global bal
    damt=float(input("Enter how amount u want to deposit: "))
    if (damt<=0):
        raise DepositError
    else:
        bal=bal+damt
        print("\n Your Account xxx123 credited with INR: {}".format((damt)))
        print("Your Account Balance INR:{}".format(bal))
def Withdraw():
    try:
        p=int(input("Enter your pin:"))
        s.execute("select *from account_details where pin=%d"%p)

    except mysql.connector.errors.InternalError:
        print("Please enter correct pin")
    else:
        global bal
        wamt=float(input("Enter How much amount u want to withdraw: "))
        if (wamt<=0):
            raise WithdrawError
        elif(wamt+500>bal):
            raise InsufficientError
        elif(wamt<=bal):
            bal=bal-wamt
            print("\n Your Account xxx123 debited with INR: {}".format(wamt))
            print("Your Account Bal INR: {}".format(bal))

def balenq():
    l=int(input("Enter pin: "))
    print("Your Account Bal INR: {}".format(bal))

