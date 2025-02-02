import pandas as pd
import requests
from io import StringIO
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to fetch data from the Google Sheet URL
def fetch_google_sheet(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.read_csv(StringIO(response.text))
        print("Columns in sheet:", data.columns)
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# Function to format the data into the required structure as a string
def format_data(data):
    formatted_data = []
    for _, row in data.iterrows():
        student_info = (
            "{\n"
            f"    rollNo: '{row['Roll No']}',\n"
            f"    password: '{row['Password']}',\n"
            f"    name: '{row['Name']}',\n"
            f"    motherName: '{row['Mother Name']}',\n"
            f"    image: '{row['Image Link']}',\n"
            f"    marks: [{', '.join(map(str, [row['Subject 1'], row['Subject 2'], row['Subject 3'], row['Subject 4'], row['Subject 5']]))}]\n"
            "},"
        )
        formatted_data.append(student_info)
    return "\n".join(formatted_data)

# Function to display the data in a GUI window
def display_data(data):
    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(data)
        root.update()  # Ensure the clipboard gets updated
        messagebox.showinfo("Copied", "Data copied to clipboard!")

    root = tk.Tk()
    root.title("Formatted Student Data")

    # Add a scrollable text widget to display the data
    text_widget = tk.Text(root, wrap=tk.WORD, height=20, width=80)
    text_widget.insert(tk.END, data)
    text_widget.config(state=tk.DISABLED)  # Make it read-only
    text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Add a copy button
    copy_button = ttk.Button(root, text="Copy Data", command=copy_to_clipboard)
    copy_button.pack(pady=10)

    root.mainloop()

# Main function to execute the script
def main():
    sheet_url = 'https://docs.google.com/spreadsheets/d/1QoLtpYXql4BCjf3fnTKSinP019WUodFtWpM0QIYBq1w/export?format=csv'
    sheet_data = fetch_google_sheet(sheet_url)

    if sheet_data is not None:
        formatted_data = format_data(sheet_data)

        # Save to file
        with open('formatted_student_data.py', 'w') as f:
            f.write("[\n")
            f.write(formatted_data)
            f.write("\n]")
            print("Formatted data has been saved to 'formatted_student_data.py'")

        # Show the formatted data in a GUI window
        display_data(f"[\n{formatted_data}\n]")

# Run the script
if __name__ == "__main__":
    main()
