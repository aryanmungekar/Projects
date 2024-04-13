import mysql.connector

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="result_management"
        )
        if connection.is_connected():
            print("Connected to MySQL!")
            return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed.")

def create_student_table(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                roll_no VARCHAR(50),
                subject1 INT,
                subject2 INT,
                subject3 INT,
                subject4 INT,
                subject5 INT
            )
        """)
        print("Student table created successfully.")
    except mysql.connector.Error as e:
        print(f"Error creating student table: {e}")

def insert_student_data(connection, cursor):
    try:
        name = input("Enter student name: ")
        roll_no = input("Enter student roll number: ")
        subject1 = int(input("Enter marks for subject 1: "))
        subject2 = int(input("Enter marks for subject 2: "))
        subject3 = int(input("Enter marks for subject 3: "))
        subject4 = int(input("Enter marks for subject 4: "))
        subject5 = int(input("Enter marks for subject 5: "))

        cursor.execute("""
            INSERT INTO students (name, roll_no, subject1, subject2, subject3, subject4, subject5)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (name, roll_no, subject1, subject2, subject3, subject4, subject5))
        connection.commit()
        print("Student data inserted successfully.")
    except mysql.connector.Error as e:
        print(f"Error inserting student data: {e}")

def search_student_by_roll_no(connection, cursor):
    try:
        roll_no = input("Enter student roll number to search: ")
        cursor.execute("""
            SELECT * FROM students WHERE roll_no = %s
        """, (roll_no,))
        result = cursor.fetchone()
        if result:
            print("Student found:")
            print(result)
        else:
            print("Student not found.")
    except mysql.connector.Error as e:
        print(f"Error searching student: {e}")

def delete_student_by_roll_no(connection, cursor):
    try:
        roll_no = input("Enter student roll number to delete: ")
        cursor.execute("""
            DELETE FROM students WHERE roll_no = %s
        """, (roll_no,))
        connection.commit()
        print("Student deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error deleting student: {e}")

def display_all_students(connection, cursor):
    try:
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()
        if results:
            print("All Students:")
            for student in results:
                print(student)
        else:
            print("No students found.")
    except mysql.connector.Error as e:
        print(f"Error displaying students: {e}")

def main():
    connection = connect_to_mysql()
    if not connection:
        return

    cursor = connection.cursor()

    create_student_table(cursor)

    while True:
        print("\n1. Add Student\n2. Search Student by Roll Number\n3. Delete Student by Roll Number\n4. Display All Students\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            insert_student_data(connection, cursor)
        elif choice == "2":
            search_student_by_roll_no(connection, cursor)
        elif choice == "3":
            delete_student_by_roll_no(connection, cursor)
        elif choice == "4":
            display_all_students(connection, cursor)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    close_connection(connection)

if __name__ == "__main__":
    main()