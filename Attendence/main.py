import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from openpyxl import Workbook
from datetime import datetime

class AttendanceApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Attendance Record App")
        self.geometry("400x300")

        self.students = ["John", "Alice", "Bob", "Emma", "David"]

        self.attendance_dict = {student: tk.BooleanVar() for student in self.students}

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Select attendance:", font=("Arial", 14))
        label.pack(pady=10)

        for student in self.students:
            check_button = tk.Checkbutton(self, text=student, variable=self.attendance_dict[student])
            check_button.pack()

        save_button = tk.Button(self, text="Save Attendance", command=self.save_attendance)
        save_button.pack(pady=20)

    def save_attendance(self):
        present_students = [student for student in self.students if self.attendance_dict[student].get()]

        # Prompt the user to enter subject and date
        subject = simpledialog.askstring("Enter Subject", "Enter the subject:")
        if not subject:
            messagebox.showwarning("Subject Required", "Please enter the subject.")
            return

        date = datetime.now().strftime("%Y-%m-%d")

        # Create a new Excel workbook and add the attendance data along with subject and date
        wb = Workbook()
        ws = wb.active

        # Add the header line with subject and date
        ws.append(["Date", "Subject", "Student Name", "Attendance"])

        for student in self.students:
            for i in range(4):
                if i == 0:
                    ws.append([date, subject if i == 1 else '', student if i == 2 else '', "Present" if student in present_students else "Absent"])

        # Save the workbook to a file
        wb.save(f"{subject}_attendance_{date}.xlsx")

        messagebox.showinfo("Attendance Saved", f"Attendance saved to {subject}_attendance_{date}.xlsx")

if __name__ == "__main__":
    app = AttendanceApp()
    app.mainloop()
