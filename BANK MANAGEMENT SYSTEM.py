# ============================================================
#                 BANK MANAGEMENT SYSTEM
# ============================================================

import random
import matplotlib.pyplot as plt
from datetime import datetime


# ============================================================
#                    PRE-STORED DATA
# ============================================================

# USER LOGIN DATA
users = {
    "rahul": "1234",
    "priya": "5678",
    "aman": "1111"
}


# ADMIN LOGIN DATA
admins = {
    "admin": "admin123"
}


# ACCOUNT DATA

accounts = {

    1000000001: {
        "name": "Rahul Sharma",
        "phone": "9876543210",
        "email": "rahul@gmail.com",
        "address": "Delhi",
        "balance": 50000,
        "loan_taken": "Yes"
    },

    1000000002: {
        "name": "Priya Singh",
        "phone": "9123456780",
        "email": "priya@gmail.com",
        "address": "Mumbai",
        "balance": 75000,
        "loan_taken": "No"
    },

    1000000003: {
        "name": "Aman Verma",
        "phone": "9988776655",
        "email": "aman@gmail.com",
        "address": "Bhopal",
        "balance": 40000,
        "loan_taken": "Yes"
    }
}


# LOAN DATA

loans = {

    1000000001: {
        "name": "Rahul Sharma",
        "loan_taken": "Yes",
        "loan_type": "Home Loan",
        "status": "Pending",
        "months_unpaid": 3
    },

    1000000003: {
        "name": "Aman Verma",
        "loan_taken": "Yes",
        "loan_type": "Education Loan",
        "status": "Clear",
        "months_unpaid": 0
    }
}


# FEEDBACK DATA


feedbacks = [

    {
        "account_no": 1000000001,
        "feedback": "Good banking service."
    },

    {
        "account_no": 1000000002,
        "feedback": "The staff was very helpful."
    }
]


# TRANSACTION HISTORY

transactions = [

    {
        "transaction_id": 101,
        "account_no": 1000000001,
        "type": "DEPOSIT",
        "amount": 50000,
        "date": "01-09-2026 10:30 AM"
    },

    {
        "transaction_id": 102,
        "account_no": 1000000001,
        "type": "WITHDRAW",
        "amount": 5000,
        "date": "05-09-2026 02:15 PM"
    },

    {
        "transaction_id": 103,
        "account_no": 1000000002,
        "type": "DEPOSIT",
        "amount": 75000,
        "date": "07-09-2026 11:00 AM"
    }
]


# LOANS TAKEN OVER YEARS

loan_over_years_data = {

    2022: 20,
    2023: 35,
    2024: 45,
    2025: 60,
    2026: 75
}


# ============================================================
#                     INTERFACE FUNCTIONS
# ============================================================

def line():
    print("=" * 70)


def heading(title):
    print("\n")
    line()
    print(title.center(70))
    line()


def pause():
    input("\nPress ENTER to continue...")


# ============================================================
#                 ACCOUNT NUMBER GENERATOR
# ============================================================

def generate_account_number():

    while True:

        number = random.randint(1000000000, 9999999999)

        if number not in accounts:
            return number


# ============================================================
#                    VIEW ACCOUNT DATA
# ============================================================

def view_data(account_no):

    heading("ACCOUNT DETAILS")

    if account_no in accounts:

        data = accounts[account_no]

        print("Account Number       :", account_no)
        print("Name of Holder       :", data["name"])
        print("Phone Number         :", data["phone"])
        print("Email                :", data["email"])
        print("Address              :", data["address"])
        print("Current Balance      :", data["balance"])
        print("Loan Taken           :", data["loan_taken"])

    else:
        print("No account found.")


# ============================================================
#                     UPDATE NAME
# ============================================================

def update_name(account_no):

    heading("UPDATE NAME")

    if account_no in accounts:

        new_name = input("Enter the updated name: ")

        accounts[account_no]["name"] = new_name

        print("\nName successfully updated.")

    else:
        print("Account not found.")


# ============================================================
#                     UPDATE EMAIL
# ============================================================

def update_email(account_no):

    heading("UPDATE EMAIL")

    if account_no in accounts:

        new_email = input("Enter the updated email: ")

        accounts[account_no]["email"] = new_email

        print("\nEmail successfully updated.")

    else:
        print("Account not found.")


# ============================================================
#                  UPDATE PHONE NUMBER
# ============================================================

def update_phone_number(account_no):

    heading("UPDATE PHONE NUMBER")

    if account_no in accounts:

        new_phone = input("Enter the updated phone number: ")

        accounts[account_no]["phone"] = new_phone

        print("\nPhone number successfully updated.")

    else:
        print("Account not found.")


# ============================================================
#                     UPDATE ADDRESS
# ============================================================

def update_address(account_no):

    heading("UPDATE ADDRESS")

    if account_no in accounts:

        new_address = input("Enter the updated address: ")

        accounts[account_no]["address"] = new_address

        print("\nAddress successfully updated.")

    else:
        print("Account not found.")


# ============================================================
#                      GIVE FEEDBACK
# ============================================================

def give_feedback(account_no):

    heading("CUSTOMER FEEDBACK")

    print("Enter your feedback below.")

    feed = input("Feedback: ")

    if feed != "":

        feedbacks.append({
            "account_no": account_no,
            "feedback": feed
        })

        print("\nThank you for your feedback!")

    else:

        print("Feedback cannot be empty.")


# ============================================================
#                  VIEW LOAN STATUS
# ============================================================

def view_loan_status(account_no):

    heading("LOAN STATUS")

    if account_no in loans:

        data = loans[account_no]

        print("Account Number       :", account_no)
        print("Account Holder Name  :", data["name"])
        print("Loan Taken           :", data["loan_taken"])
        print("Type of Loan        :", data["loan_type"])
        print("Status of Loan       :", data["status"])
        print("Months Interest Unpaid:", data["months_unpaid"])

    else:

        print("No loan data found for this account.")


# ============================================================
#                    ADD NEW ACCOUNT
# ============================================================

def add_data():

    heading("ADD NEW ACCOUNT")

    account_no = generate_account_number()

    name = input("Enter the name of account holder: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email of account holder: ")
    address = input("Enter the address of account holder: ")

    try:
        balance = float(input("Enter the initial balance: "))
    except ValueError:
        print("Invalid balance.")
        return

    loan = input("Enter whether loan taken or not (Yes/No): ")

    accounts[account_no] = {

        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "balance": balance,
        "loan_taken": loan
    }

    # Create user login automatically
    username = name.lower().replace(" ", "")

    password = str(random.randint(1000, 9999))

    users[username] = password

    print("\nSuccessfully added new account.")
    print("--------------------------------")
    print("Account Number :", account_no)
    print("Username       :", username)
    print("Password       :", password)


# ============================================================
#                   VIEW FEEDBACKS
# ============================================================

def view_feedbacks():

    heading("CUSTOMER FEEDBACK")

    if len(feedbacks) == 0:

        print("No feedback available.")

    else:

        for data in feedbacks:

            print("--------------------------------")
            print("Account Number :", data["account_no"])
            print("Feedback       :", data["feedback"])


# ============================================================
#                  VIEW LOAN DETAILS
# ============================================================

def view_loan_details():

    heading("ALL LOAN DETAILS")

    if len(loans) == 0:

        print("No loan data available.")
        return

    for account_no, data in loans.items():

        print("----------------------------------------")
        print("Account Number        :", account_no)
        print("Account Holder Name   :", data["name"])
        print("Loan Taken            :", data["loan_taken"])
        print("Type of Loan          :", data["loan_type"])
        print("Status of Loan        :", data["status"])
        print("Months Interest Unpaid:", data["months_unpaid"])


# ============================================================
#                UPDATE LOAN STATUS
# ============================================================

def update_status_loan():

    heading("UPDATE LOAN STATUS")

    try:

        number = int(input("Enter the account number: "))

    except ValueError:

        print("Invalid account number.")
        return

    if number not in loans:

        print("Loan record not found.")
        return

    print("\nCurrent Status:", loans[number]["status"])

    stat = input("Enter new loan status (Clear/Pending): ")

    if stat.lower() == "clear":

        loans[number]["status"] = "Clear"

    elif stat.lower() == "pending":

        loans[number]["status"] = "Pending"

    else:

        print("Invalid loan status.")
        return

    print("\nLoan status updated successfully.")


# ============================================================
#                   LOAN DEFAULTERS
# ============================================================

def status_loan_defaulters():

    heading("LOAN DEFAULTERS")

    try:

        months = int(
            input("Enter the number of months: ")
        )

    except ValueError:

        print("Invalid number.")
        return

    found = False

    for account_no, data in loans.items():

        if data["months_unpaid"] >= months:

            print("----------------------------------------")
            print("Account Number :", account_no)
            print("Account Holder :", data["name"])
            print("Loan Taken     :", data["loan_taken"])
            print("Loan Type      :", data["loan_type"])
            print("Loan Status    :", data["status"])
            print("Months Unpaid  :", data["months_unpaid"])

            found = True

    if not found:

        print("\nNo loan defaulters found.")


# ============================================================
#                    ADD LOAN DATA
# ============================================================

def add_data_loan():

    heading("ADD NEW LOAN DATA")

    try:

        account_no = int(
            input("Enter the account number: ")
        )

    except ValueError:

        print("Invalid account number.")
        return

    if account_no not in accounts:

        print("Account number does not exist.")
        return

    name = accounts[account_no]["name"]

    loan_amount = input("Enter amount of loan taken: ")
    loan_type = input("Enter the type of loan: ")
    status = input("Enter the status of loan: ")

    try:

        months = int(
            input(
                "Enter number of months from which "
                "interest is not paid: "
            )
        )

    except ValueError:

        print("Invalid number.")
        return

    loans[account_no] = {

        "name": name,
        "loan_taken": "Yes",
        "loan_type": loan_type,
        "status": status,
        "months_unpaid": months
    }

    accounts[account_no]["loan_taken"] = "Yes"

    print("\nSuccessfully added loan data.")


# ============================================================
#                    LOAN GRAPH
# ============================================================

def loan_over_years():

    heading("LOANS TAKEN OVER THE YEARS")

    years = list(loan_over_years_data.keys())
    loan_count = list(loan_over_years_data.values())

    plt.figure(figsize=(8, 5))

    plt.bar(years, loan_count)

    plt.xlabel("YEAR")
    plt.ylabel("LOANS TAKEN")
    plt.title("LOANS TAKEN OVER THE YEARS")

    plt.show()


# ============================================================
#                DEPOSIT / WITHDRAW MONEY
# ============================================================

def money_deposited_withdrawn(account_no):

    heading("MONEY DEPOSIT / WITHDRAW")

    if account_no not in accounts:

        print("Account not found.")
        return

    print("1. Deposit")
    print("2. Withdraw")

    try:

        choice = int(input("Enter your choice: "))

    except ValueError:

        print("Invalid choice.")
        return

    try:

        amount = float(
            input("Enter amount: ")
        )

    except ValueError:

        print("Invalid amount.")
        return

    if amount <= 0:

        print("Amount must be greater than zero.")
        return

    # ---------------- DEPOSIT ----------------

    if choice == 1:

        accounts[account_no]["balance"] += amount

        transaction_type = "DEPOSIT"

        print("\nMoney deposited successfully.")

    # ---------------- WITHDRAW ----------------

    elif choice == 2:

        if amount > accounts[account_no]["balance"]:

            print("\nInsufficient balance.")
            return

        accounts[account_no]["balance"] -= amount

        transaction_type = "WITHDRAW"

        print("\nMoney withdrawn successfully.")

    else:

        print("Invalid choice.")
        return


    # Generate transaction ID

    transaction_id = random.randint(1000, 9999)

    transaction = {

        "transaction_id": transaction_id,
        "account_no": account_no,
        "type": transaction_type,
        "amount": amount,
        "date": datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )
    }

    transactions.append(transaction)

    print("Current Balance:",
          accounts[account_no]["balance"])


# ============================================================
#                     PASSBOOK
# ============================================================

def view_passbook(account_no):

    heading("PASSBOOK")

    found = False

    print(
        f"{'ID':<10}"
        f"{'TYPE':<15}"
        f"{'AMOUNT':<15}"
        f"{'DATE':<25}"
    )

    line()

    for transaction in transactions:

        if transaction["account_no"] == account_no:

            print(
                f"{transaction['transaction_id']:<10}"
                f"{transaction['type']:<15}"
                f"{transaction['amount']:<15}"
                f"{transaction['date']:<25}"
            )

            found = True

    if not found:

        print("NO TRANSACTION FOUND FOR THIS ACCOUNT.")


# ============================================================
#                    ADMIN MENU
# ============================================================

def admin_menu():

    while True:

        heading("ADMIN MENU")

        print("1. Add New Account")
        print("2. View Loan Data")
        print("3. Update Loan Status")
        print("4. View Loan Defaulters")
        print("5. View Feedback")
        print("6. Add Loan Data")
        print("7. Loan Taken Over The Years")
        print("8. Deposit / Withdraw Money")
        print("9. Exit")

        line()

        try:

            ch = int(input("Enter your choice: "))

        except ValueError:

            print("Please enter a valid number.")
            continue


        if ch == 1:

            add_data()
            pause()


        elif ch == 2:

            view_loan_details()
            pause()


        elif ch == 3:

            update_status_loan()
            pause()


        elif ch == 4:

            status_loan_defaulters()
            pause()


        elif ch == 5:

            view_feedbacks()
            pause()


        elif ch == 6:

            add_data_loan()
            pause()


        elif ch == 7:

            loan_over_years()
            pause()


        elif ch == 8:

            try:

                number = int(
                    input("Enter the account number: ")
                )

                money_deposited_withdrawn(number)

                view_passbook(number)

            except ValueError:

                print("Invalid account number.")

            pause()


        elif ch == 9:

            print("\nLogging out from Admin Panel...")
            break


        else:

            print("\nInvalid choice.")


# ============================================================
#                    USER MENU
# ============================================================

def user_menu(account_no):

    while True:

        heading("USER MENU")

        print("Account Number:", account_no)
        print("1. View Account")
        print("2. Update Name")
        print("3. Update Email")
        print("4. Update Phone Number")
        print("5. Update Address")
        print("6. Give Feedback")
        print("7. View Loan Status")
        print("8. Loan Taken Over The Years")
        print("9. Deposit / Withdraw Money")
        print("10. View Passbook")
        print("11. Logout")

        line()

        try:

            ch = int(input("Enter your choice: "))

        except ValueError:

            print("Please enter a valid number.")
            continue


        if ch == 1:

            view_data(account_no)
            pause()


        elif ch == 2:

            update_name(account_no)
            pause()


        elif ch == 3:

            update_email(account_no)
            pause()


        elif ch == 4:

            update_phone_number(account_no)
            pause()


        elif ch == 5:

            update_address(account_no)
            pause()


        elif ch == 6:

            give_feedback(account_no)
            pause()


        elif ch == 7:

            view_loan_status(account_no)
            pause()


        elif ch == 8:

            loan_over_years()
            pause()


        elif ch == 9:

            money_deposited_withdrawn(account_no)
            pause()


        elif ch == 10:

            view_passbook(account_no)
            pause()


        elif ch == 11:

            print("\nLogging out...")
            break


        else:

            print("\nInvalid choice.")


# ============================================================
#                    ADMIN LOGIN
# ============================================================

def admin_login():

    heading("ADMIN LOGIN")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in admins:

        if admins[username] == password:

            print("\nLogin Successful!")

            pause()

            admin_menu()

        else:

            print("\nIncorrect password.")

    else:

        print("\nInvalid username.")


# ============================================================
#                     USER LOGIN
# ============================================================

def user_login():

    heading("USER LOGIN")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:

        if users[username] == password:

            # Find account belonging to username

            account_found = False

            for account_no, data in accounts.items():

                generated_username = (
                    data["name"].lower().replace(" ", "")
                )

                if generated_username == username:

                    print("\nLogin Successful!")

                    pause()

                    user_menu(account_no)

                    account_found = True
                    break

            if not account_found:

                print("Account data not found.")

        else:

            print("\nIncorrect password.")

    else:

        print("\nInvalid username.")


# ============================================================
#                     MAIN MENU
# ============================================================

def main():

    while True:

        heading("WELCOME TO BANK MANAGEMENT SYSTEM")

        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")

        line()

        try:

            choice = int(
                input("Enter your choice: ")
            )

        except ValueError:

            print("\nPlease enter a valid number.")
            continue


        # ADMIN

        if choice == 1:

            admin_login()


        # USER

        elif choice == 2:

            user_login()


        # EXIT

        elif choice == 3:

            print("\n")
            line()
            print(
                "THANK YOU FOR USING BANK MANAGEMENT SYSTEM"
                .center(70)
            )
            line()

            break


        else:

            print("\nInvalid choice.")


main()