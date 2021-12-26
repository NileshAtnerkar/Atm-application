import mysql.connector
def close():
    try:
        import mysql.connector
        con=mysql.connector.connect(host="localhost",user="root",password="Nilesh@123",database="Atm")
        s =con.cursor()
        k=int(input("Delete your AC enter your Account No: "))
        x=("delete from account_details where ac_number=%d"%k)
        s.execute(x)
        con.commit()

    except mysql.connector.DatabaseError:
        print("Your data is not present")

    except ValueError:
        print("Dont enters strs/special symbols and alphanumeric numbers")
    else:
        print("Your Account Deleted sucessfully!")

