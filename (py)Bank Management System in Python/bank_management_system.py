import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='12345678', database='BANK_MANAGEMENT')

def OpenAcc():
    n = input("Enter the name: ")
    ac = input("Enter account no: ")
    db = input("Enter Date of Birth: ")
    add = input("Enter the Address: ")
    cn = input("Enter Contact No: ")
    ob = int(input("Enter the Opening Balance: "))
    data1 = (n, ac, db, add, cn, ob)
    data2 = (n, ac, ob)
    sql1 = 'INSERT INTO account VALUES (%s, %s, %s, %s, %s, %s)'
    sql2 = 'INSERT INTO amount VALUES (%s, %s, %s)'
    cursor = mydb.cursor()
    cursor.execute(sql1, data1)
    cursor.execute(sql2, data2)
    mydb.commit()
    print("Data Entered Successfully")
    main()  

def DepoAmo():
    amount = input("Enter the amount you want to deposit: ")
    ac = input("Enter the Account no: ")
    sql_select = 'SELECT balance FROM amount WHERE AccNo = %s'
    data = (ac,)
    cursor = mydb.cursor()
    cursor.execute(sql_select, data)
    result = cursor.fetchone()
    if result:
        current_balance = result[0]
        new_balance = current_balance + int(amount)
        sql_update = 'UPDATE amount SET balance = %s WHERE AccNo = %s'
        update_data = (new_balance, ac)
        cursor.execute(sql_update, update_data)
        mydb.commit()
        print("Amount deposited successfully.")
    else:
        print("Account not found.")
    main()

def WithdrawAmount():
    amount = input("Enter the amount you want to withdraw: ")
    ac = input("Enter the Account no: ")
    sql_select = 'SELECT balance FROM amount WHERE AccNo = %s'
    data = (ac,)
    cursor = mydb.cursor()
    cursor.execute(sql_select, data)
    result = cursor.fetchone()
    if result:
        current_balance = result[0]
        if current_balance >= int(amount):
            new_balance = current_balance - int(amount)
            sql_update = 'UPDATE amount SET balance = %s WHERE AccNo = %s'
            update_data = (new_balance, ac)
            cursor.execute(sql_update, update_data)
            mydb.commit()
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")
    main()

def BalEnq():
    ac = input("Enter Account Number: ")
    sql_select = 'SELECT balance FROM amount WHERE AccNo = %s'
    data = (ac,)
    cursor = mydb.cursor()
    cursor.execute(sql_select, data)
    result = cursor.fetchone()
    if result:
        print("Balance for Account no ", ac, " is", result[0])
    else:
        print("Account not found.")
    main()

def DisDetails():
    ac = input("Enter Account Number: ")
    sql_select = 'SELECT * FROM account WHERE AccNo = %s'
    data = (ac,)
    cursor = mydb.cursor()
    cursor.execute(sql_select, data)
    result = cursor.fetchone()
    if result:
        print("Customer Details:")
        for i in result:
            print(i)
    else:
        print("Account not found.")
    main()

def CloseAcc():
    ac = input("Enter Account Number: ")
    sql_delete_account = 'DELETE FROM account WHERE AccNo = %s'
    sql_delete_amount = 'DELETE FROM amount WHERE AccNo = %s'
    data = (ac,)
    cursor = mydb.cursor()
    cursor.execute(sql_delete_account, data)
    cursor.execute(sql_delete_amount, data)
    mydb.commit()
    print("Account Closed Successfully")
    main()

def main():
    print('''
                1. OPEN NEW ACCOUNT
                2. DEPOSIT AMOUNT
                3. WITHDRAW AMOUNT
                4. BALANCE ENQUIRY
                5. DISPLAY CUSTOMER DETAILS 
                6. CLOSE AN ACCOUNT
                ''')
    choice = input("Please enter your choice: ")
    if choice == '1':
        OpenAcc()
    elif choice == '2':
        DepoAmo()
    elif choice == '3':
        WithdrawAmount()
    elif choice == '4':
        BalEnq()
    elif choice == '5':
        DisDetails()
    elif choice == '6':
        CloseAcc()
    else:
        print("Invalid Choice")
        main()

if __name__ == "__main__":
    main()
