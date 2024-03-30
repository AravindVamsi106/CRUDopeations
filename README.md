                              CRUD Operations in the Registration Database
This Python script allows the user to perform CRUD (Create, Read, Update, Delete) operations on a SQLite Database table “Register”. Command Line Interface is provided to perform the operations.
Prerequisites:
SQLite3 module for Python 3.x (pre-installed with Python)
Configuration
To save the repository on your local computer, download or clone it.
Make sure your computer is running Python.
Python’s standard library has the SQLite3 module, thus no further installation is needed.
Steps to Follow:
1) Download the file provided to your local computer.
2) Double click on the downloaded file to run the script
			Or
     Launch a command prompt or terminal & open the directory where the registration_operations.py Python script is located and run the following command:
                         python registration_operations.py.
3)To create a new record, select option 1 and fill out the necessary fields (name, email, and birthdate).
4) To read all the records in the table, select option 2
5) To update the existing record, select option 3 and provide the ID(Primary key) and the values to be updated.
6) To delete a record from the table, select option 4 and provide the ID of the record you want to delete.
7) To exit from the menu, select 5.

Options
•	Create a new record: Enter option 1 and provide the required information (name, email, date of birth).
•	Read all records: Enter option 2 to view all records in the "Register" table.
•	Update a record: Enter option 3 and provide the ID of the record you want to update, along with the updated information (name, email, date of birth).
•	Delete a record: Enter option 4 and provide the ID of the record you want to delete.
•	Exit: Enter option 5 to exit the program.

Note
•	The SQLite database file (registration.db) will be created in the same directory as the Python script.
•	Ensure you have appropriate permissions to read and write files in the directory.
•	Make sure to enter date values in the format YYYY-MM-DD when prompted.
•	If any error occurred then an exception message will be thrown, 
•	1.If an error occurred while creating (inserting) the record then it will throw “Error inserting record” exception
•	2. If an error occurred while performing read operation then it will throw “Error reading records” exception
•	3. If an error occurred while updating data then it will throw “Error updating record” exception
•	4. If an error occurred while deleting any record from the table then it will throw “Error deleting record” exception.
•	5. If an error occurred while creating the table then it will throw “Error creating table” exception.
