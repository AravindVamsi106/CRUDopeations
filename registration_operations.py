import sqlite3
from datetime import datetime

# Function to create the Registration table
def create_table():
    try:
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Register (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT NOT NULL,
                        Email TEXT NOT NULL,
                        DateOfBirth DATE
                    )''')
        conn.commit()
    except sqlite3.Error as e:
        print("Error creating table:", e)
    finally:
        conn.close()

# Function to insert a new record into the Registration table
def create_record():
    try:
        name = input("Enter name: ")
        email = input("Enter email: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute('''INSERT INTO Register (Name, Email, DateOfBirth)
                        VALUES (?, ?, ?)''', (name, email, dob))
        conn.commit()
    except sqlite3.Error as e:
        print("Error inserting record:", e)
    finally:
        conn.close()

# Function to retrieve records from the Registration table
def read_records():
    try:
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM Register''')
        records = c.fetchall()
        return records
    except sqlite3.Error as e:
        print("Error reading records:", e)
    finally:
        conn.close()

# Function to update a record in the Registration table
def update_record():
    try:
        record_id = int(input("Enter ID of record to update: "))
        name = input("Enter updated name: ")
        email = input("Enter updated email: ")
        dob = input("Enter updated date of birth (YYYY-MM-DD): ")
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute('''UPDATE Register 
                        SET Name=?, Email=?, DateOfBirth=? 
                        WHERE ID=?''', (name, email, dob, record_id))
        conn.commit()
    except sqlite3.Error as e:
        print("Error updating record:", e)
    finally:
        conn.close()

# Function to delete a record from the Registration table
def delete_record():
    try:
        record_id = int(input("Enter ID of record to delete: "))
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute('''DELETE FROM Register WHERE ID=?''', (record_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("Error deleting record:", e)
    finally:
        conn.close()

# Sample usage
if __name__ == "__main__":
    create_table()
    
# displaying the menu and performing the operations according to the user input.
    while True:
        print("\nChoose an option:")
        print("1. Create a new record")
        print("2. Read all records")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_record()
        elif choice == '2':
            print("\nRecords:")
            for record in read_records():
                print(record)
        elif choice == '3':
            update_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
