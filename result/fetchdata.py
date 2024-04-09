import tkinter as tk
from tkinter import scrolledtext

import pandas as pd

def fetch_student_data_from_excel(file_path):
    try:
        # Read data from Excel file into a DataFrame
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    # Initialize a list to store student data
    students = []

    # Iterate over each row in the DataFrame
    for _, row in df.iterrows():
        # Extract student data from the current row
        student = {
            'rollNo': str(row['Roll No']),
            'password': str(row['Password']),
            'name': str(row['Name']),
            'motherName': str(row["Mother's Name"]),
            'image': str(row['Image URL']),
            'marks': [int(row[f'Subject {i+1}']) for i in range(5)]  # Assuming there are 5 subjects
        }

        # Append student data to the list
        students.append(student)

    return students

def generate_code():
    # Fetch student data from the Excel file
    students = fetch_student_data_from_excel('students.xlsx')

    code = ""
    # Generate student data code
    for student in students:
        code += "{\n"
        code += f"    rollNo: '{student['rollNo']}',\n"
        code += f"    password: '{student['password']}',\n"
        code += f"    name: '{student['name']}',\n"
        code += f"    motherName: '{student['motherName']}',\n"
        code += f"    image: '{student['image']}',\n"
        code += f"    marks: {student['marks']}\n"
        code += "},\n"

    # Display the code in a separate window
    root = tk.Tk()
    root.title("Generated Code")

    text_area = scrolledtext.ScrolledText(root, width=80, height=30, wrap=tk.WORD)
    text_area.insert(tk.INSERT, code)
    text_area.pack()

    copy_button = tk.Button(root, text="Copy Code", command=lambda: root.clipboard_append(code))
    copy_button.pack()

    root.mainloop()

if __name__ == "__main__":
    generate_code()
