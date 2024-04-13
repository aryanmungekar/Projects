import tkinter as tk
from tkinter import messagebox, simpledialog
from openpyxl import Workbook
from datetime import datetime

class AttendanceApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Attendance Record App")
        self.geometry("400x400")

        self.students = ["John", "Alice", "Bob", "Emma", "David"]

        self.attendance_dict = {student: tk.BooleanVar() for student in self.students}

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Select attendance:", font=("Arial", 14))
        label.pack(pady=10)

        for student in self.students:
            check_button = tk.Checkbutton(self, text=student, variable=self.attendance_dict[student], font=("Arial", 12))
            check_button.pack(anchor=tk.W, padx=10, pady=5)

        save_button = tk.Button(self, text="Save Attendance", command=self.save_attendance, font=("Arial", 12), bg="green", fg="white")
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
            ws.append([date, subject, student, "Present" if student in present_students else "Absent"])

        # Save the workbook to a file
        filename = f"{subject}_attendance_{date}.xlsx"
        wb.save(filename)

        messagebox.showinfo("Attendance Saved", f"Attendance saved to {filename}")

if __name__ == "__main__":
    app = AttendanceApp()
    app.mainloop()
