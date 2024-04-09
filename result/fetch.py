import pandas as pd

def fetch_student_data_from_excel(file_path):
    # Read data from Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Initialize a list to store student data
    students = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
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

def main():
    # Path to the Excel file containing student data
    excel_file_path = 'students.xlsx'

    # Fetch student data from the Excel file
    students = fetch_student_data_from_excel(excel_file_path)

    # Print student data in the specified format
    for student in students:
        print("{")
        print("    rollNo:", repr(student['rollNo']) + ",")
        print("    password:", repr(student['password']) + ",")
        print("    name:", repr(student['name']) + ",")
        print("    motherName:", repr(student['motherName']) + ",")
        print("    image:", repr(student['image']) + ",")
        print("    marks:", student['marks'])
        print("},")

if __name__ == "__main__":
    main()
