import os
import mysql.connector
import random
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user=os.environ.get("user"),
    passwd=os.environ.get("passwd"),
    database=os.environ.get("dbName")
)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE Transactions (id int PRIMARY KEY AUTO_INCREMENT, date DATETIME, accountId int, FOREIGN KEY(accountId) REFERENCES Customer(id), title varchar(80), type varchar(20), total double NOT NULL)")

def menu():
    print("\v        CUSTOMER ACCOUNT BANKING MANAGEMENT SYSTEM\v")
    print("        ---------WELCOME TO THE MAIN MENU--------- \v")
    print("1. Create new account")
    print("2. Update information of existing account")
    print("3. For transaction")
    print("4. Check the details existing account")
    print("5. Removing existing account")
    print("6. View customer list")
    print("7. Exit \v")

    choice = input("Enter your choice: ")
    
    if(int(choice) == 1):
        createAccount()
    elif(int(choice) == 2):
        updateInfo()
    elif(int(choice) == 3):
        transaction()
    elif(int(choice)  == 4 ):
        checkAccount()
    elif(int(choice) == 5):
        removeAccount()
    elif(int(choice) == 6):
        viewCustomers()
    elif(int(choice) == 7):
        exit
    else:
        print("You Entered an Invalid Number. Try Again.")
        print(">------------------------------------------------")
        menu()

def createAccount():
    id = random.randint(0, 1000000)
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    birth_date = input("Date of birth (YYYY-MM-DD): ")
    age = input("Age: ")
    ssn = input("SSN: ")
    gender = input("Gender ('M','F','O'): ")
    address = input("Address: ")
    phoneNumber = input("Phone Number: ")
    depositAmount= input("Depoise Amount: ")
    typeOfAccount = input("Type of Account (S','C','F1','F2','F3'): ")

    data =(id, firstName, lastName, birth_date, int(age), int(ssn), gender, address, phoneNumber, depositAmount, typeOfAccount ) 
    sql_insert = "INSERT INTO Customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor = mydb.cursor()
    mycursor.execute(sql_insert,data)
    mydb.commit()

    print(">\v------------------------------------------------")
    print("Acoount Successfully Created!")
    print(">------------------------------------------------\v")
    taskDonePrompt()

def updateInfo():
    print("updating Information!!!!!!!!!!!!!!!!!!!!")

    print("ENTER A TASK NUMBER")
    print(">------------------------------------------------")
    print("1. UPDATE Phone Number")
    print("2. UPDATE Address")
    print("3. CANCEL UPDATE")
    choice = input("Enter your choice: ")

    if(int(choice) == 1):
        personToUpdate = input("What is the last name of the Person you want to update? ")
        replaceValue = input("What is the new phone number? ")
        mycursor = mydb.cursor()
        mycursor.execute('SELECT lastName FROM Customer WHERE lastName = %s', (personToUpdate,))
        checklastName = mycursor.fetchone()
        if not checklastName:
            print('lastName does not exist cannot Update')
        else:
            mycursor.execute("UPDATE Customer SET phoneNumber = %s WHERE lastName = %s", (replaceValue, personToUpdate ))
            mydb.commit()
            print(">------------------------------------------------")
            print("Phone Number was Successfully Updated")
            print(">------------------------------------------------")
            taskDonePrompt()
    elif(int(choice) == 2):
        personToUpdate = input("What is the last name of the Person you want to update? ")
        replaceValue = input("What is the new adress? ")
        mycursor = mydb.cursor()
        mycursor.execute('SELECT lastName FROM Customer WHERE lastName = %s', (personToUpdate,))
        checklastName = mycursor.fetchone()
        if not checklastName:
            print('lastName does not exist cannot Update')
        else:
            mycursor.execute("UPDATE Customer SET address = %s WHERE lastName = %s", (replaceValue, personToUpdate ))
            mydb.commit()
            print(">------------------------------------------------")
            print("Address was Successfully Updated")
            print(">------------------------------------------------")
            taskDonePrompt()
    elif(int(choice) == 3):
        menu()
    else:
        print("You Entered an Invalid Number. Try Again.")
        print(">------------------------------------------------")
        updateInfo()


def transaction():
    mycursor = mydb.cursor()

    accountNumeber = input("What is your account number? ")
    typeOfTransaction = input("What type of transaction is this? (Deposit or Withdrawing) ")
    title = input("What is the name of this transaction? ")
    amount = input("What is the amount that you are Depositing or Withdrawing? ")
    date = datetime.now()

    formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')

    mycursor.execute('SELECT id FROM Customer WHERE id = %s', (int(accountNumeber),))

    checkId = mycursor.fetchone()
    if not checkId:
        print('Account Number does not exist\v')
        answer = input("Do you want to Try Agin? (Y or N): ")
        if (answer == 'Y' or 'y'):
            transaction()
        elif (answer == "N" or 'n'):
            menu()
        else:
            print("Invaild Command. Try Again.")
            menu()
    else:
        data =(formatted_date, int(accountNumeber), title, typeOfTransaction, float(amount) ) 
        sql_insert = "INSERT INTO Transactions (date, accountId, title, type, total) VALUES (%s,%s,%s,%s,%s)"
        
        mycursor.execute(sql_insert,data)
        mydb.commit()

        print(">\v------------------------------------------------")
        print("Transaction Complete!")
        print(">------------------------------------------------\v")

    taskDonePrompt()


def checkAccount():
    print("transaction completed")

def removeAccount():
    personToDelete = input("What is the lastName of the Customer you want to delete? ")
    mycursor = mydb.cursor()

    mycursor.execute('SELECT lastName FROM Customer WHERE lastName = %s', (personToDelete,))

    checklastName = mycursor.fetchone()
    if not checklastName:
        print('lastName does not exist')
    else:
        mycursor.execute("DELETE FROM Customer WHERE lastName = %s", (personToDelete,))
        mydb.commit()
        print(">------------------------------------------------")
        print("Customer was Successfully Deleted")
        print(">------------------------------------------------")
        
    taskDonePrompt()

def viewCustomers():
    print("\v")
    print("Customer List")

    mycursor = mydb.cursor()
    mycursor.execute("SELECT firstName, lastName, address, phoneNumber FROM Customer")
    for i in mycursor:
      print(">------------------------------------------------")
      print(i)

    print("\v")
    taskDonePrompt()

def taskDonePrompt():
    answer = input("Do you want to perform another task? (Y or N): ")
    if (answer == 'Y' or 'y'):
        menu()
    elif (answer == "N" or 'n'):
        exit()
    else:
        print("Invaild Command. Try Again.")
        taskDonePrompt()

menu()    