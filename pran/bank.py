import tkinter as tk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='BANK_MANAGEMENT'
)

def OpenAcc(root):
    def submit():
        n = name_entry.get()
        ac = acc_entry.get()
        db = dob_entry.get()
        add = address_entry.get()
        cn = contact_entry.get()
        ob = int(open_bal_entry.get())
        data1 = (n, ac, db, add, cn, ob)
        data2 = (n, ac, ob)
        sql1 = 'INSERT INTO account VALUES (%s, %s, %s, %s, %s, %s)'
        sql2 = 'INSERT INTO amount VALUES (%s, %s, %s)'
        cursor = mydb.cursor()
        cursor.execute(sql1, data1)
        cursor.execute(sql2, data2)
        mydb.commit()
        messagebox.showinfo("Success", "Account opened successfully.")

    open_acc_window = tk.Toplevel(root)
    open_acc_window.title("Open New Account")

    name_label = tk.Label(open_acc_window, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(open_acc_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    acc_label = tk.Label(open_acc_window, text="Account No:")
    acc_label.grid(row=1, column=0, padx=5, pady=5)
    acc_entry = tk.Entry(open_acc_window)
    acc_entry.grid(row=1, column=1, padx=5, pady=5)

    dob_label = tk.Label(open_acc_window, text="Date of Birth:")
    dob_label.grid(row=2, column=0, padx=5, pady=5)
    dob_entry = tk.Entry(open_acc_window)
    dob_entry.grid(row=2, column=1, padx=5, pady=5)

    address_label = tk.Label(open_acc_window, text="Address:")
    address_label.grid(row=3, column=0, padx=5, pady=5)
    address_entry = tk.Entry(open_acc_window)
    address_entry.grid(row=3, column=1, padx=5, pady=5)

    contact_label = tk.Label(open_acc_window, text="Contact No:")
    contact_label.grid(row=4, column=0, padx=5, pady=5)
    contact_entry = tk.Entry(open_acc_window)
    contact_entry.grid(row=4, column=1, padx=5, pady=5)

    open_bal_label = tk.Label(open_acc_window, text="Opening Balance:")
    open_bal_label.grid(row=5, column=0, padx=5, pady=5)
    open_bal_entry = tk.Entry(open_acc_window)
    open_bal_entry.grid(row=5, column=1, padx=5, pady=5)

    submit_btn = tk.Button(open_acc_window, text="Submit", command=submit)
    submit_btn.grid(row=6, columnspan=2, padx=5, pady=5)

def WithdrawAcc(root):
    def withdraw():
        amount = withdraw_entry.get()
        ac = acc_entry.get()
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
                messagebox.showinfo("Success", "Amount withdrawn successfully.")
            else:
                messagebox.showerror("Error", "Insufficient balance.")
        else:
            messagebox.showerror("Error", "Account not found.")

    withdraw_window = tk.Toplevel(root)
    withdraw_window.title("Withdraw Amount")

    acc_label = tk.Label(withdraw_window, text="Account No:")
    acc_label.grid(row=0, column=0, padx=5, pady=5)
    acc_entry = tk.Entry(withdraw_window)
    acc_entry.grid(row=0, column=1, padx=5, pady=5)

    withdraw_label = tk.Label(withdraw_window, text="Amount to Withdraw:")
    withdraw_label.grid(row=1, column=0, padx=5, pady=5)
    withdraw_entry = tk.Entry(withdraw_window)
    withdraw_entry.grid(row=1, column=1, padx=5, pady=5)

    withdraw_btn = tk.Button(withdraw_window, text="Withdraw", command=withdraw)
    withdraw_btn.grid(row=2, columnspan=2, padx=5, pady=5)

def main():
    root = tk.Tk()
    root.title("Bank Management System")

    menu_frame = tk.Frame(root)
    menu_frame.pack(padx=10, pady=10)

    open_acc_btn = tk.Button(menu_frame, text="Open New Account", command=lambda: OpenAcc(root))
    open_acc_btn.grid(row=0, column=0, padx=5, pady=5)

    withdraw_btn = tk.Button(menu_frame, text="Withdraw Amount", command=lambda: WithdrawAcc(root))
    withdraw_btn.grid(row=1, column=0, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
