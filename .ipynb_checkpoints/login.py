# Import the sqlite3 module to work with SQLite databases
import sqlite3

# Connect to the SQLite database named "hospital.db"
# If the database does not exist, it will be created automatically
conn = sqlite3.connect("hospital.db")

# Create a cursor object
# The cursor is used to execute SQL commands
cursor = conn.cursor()

# Create a table named "patients" if it does not already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    first_name TEXT,                       
    last_name TEXT,                        
    age INTEGER,                           
    gender TEXT,                           
    diagnosis TEXT                         
""")

# Save (commit) the table creation to the database
conn.commit()


# Function to register (add) a new patient
def register_patient():
    # Display section title
    print("\n--- Register New Patient ---")

    # Ask user to enter patient details
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))       # Convert age input to integer
    gender = input("Gender: ")
    diagnosis = input("Diagnosis: ")

    # Insert the patient data into the patients table
    # ? placeholders are used to prevent SQL injection
    cursor.execute("""
    INSERT INTO patients (first_name, last_name, age, gender, diagnosis)
    VALUES (?, ?, ?, ?, ?)
    """, (first_name, last_name, age, gender, diagnosis))

    # Save the inserted record to the database
    conn.commit()

    # Confirm successful registration
    print("Patient registered successfully!")


# Function to view all patients
def view_patients():
    # Display section title
    print("\n--- Patient List ---")

    # Select all records from the patients table
    cursor.execute("SELECT * FROM patients")

    # Fetch all rows returned by the query
    patients = cursor.fetchall()

    # If no patients exist, show message
    if not patients:
        print("No patients found.")
    else:
        # Loop through each patient record and print it
        for patient in patients:
            print(patient)


# Main program loop (runs continuously until user exits)
while True:
    # Display menu options
    print("\n--- Hospital Patient System ---")
    print("1. Register patient")
    print("2. View patients")
    print("3. Exit")

    # Get user choice
    choice = input("Choose option: ")

    # Call appropriate function based on user choice
    if choice == "1":
        register_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        print("Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid choice")

# Close the database connection when the program ends
conn.close()

