import mysql.connector
import random
import os

mydb = mysql.connector.connect(
    host="localhost",
    user=os.environ.get("user"),
    passwd=os.environ.get("passwd"),
    database=os.environ.get("dbName")
)

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
    elif(int(choice == 2)):
        updateInfo()
    elif(int(choice) == 3):
        transaction()
    elif(int(choice == 4)):
        checkAccount()
    elif(int(choice == 5)):
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
    print("info updated")

def transaction():
    print("transaction completed")

def checkAccount():
    print("transaction completed")

def removeAccount():
    print("transaction completed")

def viewCustomers():
    print(">\v------------------------------------------------")
    print("Customer List")
    print(">------------------------------------------------\v")

    mycursor = mydb.cursor()
    mycursor.execute("SELECT firstName, lastName, address, phoneNumber FROM Customer")
    for i in mycursor:
      print(i)

    taskDonePrompt()

def taskDonePrompt():
    answer = input("Do you want to perform another task? (Y or N): ")
    if (answer == 'Y'):
        menu()
    elif (answer == "N"):
        exit()
    else:
        print("Invaild Command. Try Again.")
        taskDonePrompt()

menu()    