import random
import mysql.connector

def createac():

    try:
        con=mysql.connector.connect(host="localhost",user="root",password="Nilesh@123",database="Atm")
        s = con.cursor()
        print("-"*50)
        print("Create Account please enter the follows details:")
        print("-" * 50)
        name=str(input("Enter your Name: "))
        mobile=int(input("Enter your mobile no: "))
    except mysql.connector.IntegrityError:
        print("Your Mobile no is already satisfied-try another number")
    except mysql.connector.errors.InterfaceError:
        print()
    except ValueError:
        print("please fill the correct details")

    else:
        if name.isdigit():
            print("Please do not include digits in your name")
        else:

            pn=random.randint(1000,9999)
            ran = random.randint(10000000, 99999999)
            s.execute("insert into Account_details values('%s',%d,%d,%d)" % (name, mobile, ran,pn))
            con.commit()
            print("-" * 50)
            print("Account Holder name is:",name)
            print("Mobile no:",mobile)
            print("-" * 50)
            print("\tyour account created successfully!")
            print("-" * 50)
            print("\nYour Account number is:",ran)
            print("\nYour Pin is: ",pn)



