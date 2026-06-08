from db_connect import conn, cursor

# Function 1
def view_expenses():

    cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()

    print("\n--- EXPENSE DETAILS ---")

    for row in rows:
        print("\n----------------------")
        print("ID       :", row[0])
        print("Name     :", row[1])
        print("Category :", row[2])
        print("Amount   :", row[3])
        print("Date     :", row[4])
        print("----------------------")


# Function 2
def add_expense():

    id = int(input("Enter Expense ID: "))

    cursor.execute(
        "SELECT * FROM expenses WHERE id = %s",
        (id,)
    )

    if cursor.fetchone():
        print("Expense ID already exists!")
        return

    name =input("Enter Expense Name: ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    exp_date = input("Enter Date (YYYY-MM-DD): ")

    query = """
    INSERT INTO expenses
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (id,
        name,
        category,
        amount,
        exp_date
    )

    cursor.execute(query, values)
    conn.commit()

    print("Expense Added Successfully!")


# Function 3
def search_expense():

    id = int(input("Enter Expense ID: "))

    query = """
    SELECT * FROM expenses
    WHERE id = %s
    """

    cursor.execute(query, (id,))

    result = cursor.fetchone()

    if result:
        print("\nExpense Found:")
        print(result)
    else:
        print("Expense Not Found")
def update_expense():

    id = int(input("Enter Expense ID: "))
    new_amount = float(input("Enter New Amount: "))

    query = """
    UPDATE expenses
    SET amount = %s
    WHERE id = %s
    """

    cursor.execute(query, (new_amount, id))
    conn.commit()

    print("Expense Updated Successfully!")

def delete_expense():

    id = int(input("Enter Expense ID: "))

    query = "DELETE FROM expenses WHERE id = %s"

    cursor.execute(query, (id,))
    conn.commit()

    print("Expense Deleted Successfully!")

def total_expenses():

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    print("Total Expenses:", total)

def highest_expense():

    cursor.execute("SELECT MAX(amount) FROM expenses")

    highest = cursor.fetchone()[0]

    print("Highest Expense:", highest)

def category_summary():

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    rows = cursor.fetchall()

    print("\nCATEGORY-WISE SUMMARY")

    for row in rows:
        print(row[0], ":", row[1])

def monthly_summary():

    cursor.execute("""
        SELECT MONTH(exp_date), SUM(amount)
        FROM expenses
        GROUP BY MONTH(exp_date)
    """)

    rows = cursor.fetchall()

    print("\nMONTHLY EXPENSE SUMMARY")

    for row in rows:
        print("Month", row[0], ":", row[1])
def expense_count():

    cursor.execute("SELECT COUNT(*) FROM expenses")

    count = cursor.fetchone()[0]

    print("Total Number of Expenses:", count)

def lowest_expense():

    cursor.execute("SELECT MIN(amount) FROM expenses")

    lowest = cursor.fetchone()[0]

    print("Lowest Expense:", lowest)

def expenses_above_amount():

    amount = float(input("Enter Amount: "))

    cursor.execute(
        "SELECT * FROM expenses WHERE amount > %s",
        (amount,)
    )

    rows = cursor.fetchall()

    if rows:

        print("\nEXPENSES ABOVE", amount)

        for row in rows:
            print(row[1], "-", row[3])

    else:
        print("No Expenses Found")
def search_by_category():

    category = input("Enter Category: ")

    cursor.execute(
        "SELECT * FROM expenses WHERE category = %s",
        (category,)
    )

    rows = cursor.fetchall()

    if rows:

        print("\nEXPENSES IN", category.upper())

        for row in rows:
            print(row[1], "-", row[3])

    else:
        print("No Expenses Found")

def average_expense():

    cursor.execute("SELECT AVG(amount) FROM expenses")

    avg = cursor.fetchone()[0]

    print("Average Expense:", round(float(avg), 2))

# Menu
while True:

    print("\nPERSONAL EXPENSE TRACKER")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. total Expenses")
    print("7. highest Expense")
    print("8. category Summary")
    print("9. monthly Summary")
    print("10. expense Count")
    print("11. lowest Expense")
    print("12. expenses above amount")
    print("13. search by category")
    print("14. average Expense")
    print("15. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        view_expenses()

    elif choice == 2:
        add_expense()

    elif choice == 3:
        search_expense()

    elif choice == 4:
        update_expense()

    elif choice == 5:
        delete_expense()

    elif choice == 6:
        total_expenses()

    elif choice == 7:
        highest_expense()

    elif choice == 8:
        category_summary()

    elif choice == 9:
        monthly_summary()

    elif choice == 10:
        expense_count()

    elif choice == 11:
        lowest_expense()

    elif choice == 12:
        expenses_above_amount()

    elif choice == 13:
        search_by_category()

    elif choice == 14:
        average_expense()

    elif choice == 15:
        print("Thank You!")
        cursor.close()
        conn.close()
        break

    else:
        print("Invalid Choice")