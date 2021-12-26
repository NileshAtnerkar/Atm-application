from atmmenu import menu
from createac import createac
from slp import sl
from exceptions import DepositError,WithdrawError,InsufficientError
from operations import deposit,Withdraw
from closeac import close
from operations import balenq
import sys
while(True):
    try:
        menu()
        ch=int(input("Enter your choice: "))
    except ValueError:
        print("Dont enters strs/special symbols and alphanumeric numbers")
    else:
        if (ch==1):
            try:
                createac()
            except Exception:
                print("please fill the correct details")
        elif(ch==2):
            try:
                deposit()
            except DepositError:
                print("Dont try to deposit -ve/zero values")
            except ValueError:
                print("Dont enter strs/special symbol and alphanumeric for deposited")

        elif(ch==3):
            try:
                Withdraw()
            except WithdrawError:
                print("Don't try to withdraw -ve/zero values")
            except InsufficientError:
                print("You dont have sufficeint funds")
            except ValueError:
                print("Dont enter strs/special symbol and alphanumeric for deposited")
        elif(ch==4):
            balenq()
        elif(ch==7):
            close()
        elif(ch==8):
            sl()
        elif(ch == 9):
            print("Thanks for using this ATM!")
            sys.exit()


