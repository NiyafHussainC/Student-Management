import tkinter as tk
from tkinter import ttk, messagebox
from student import Student
from database import Database

class StudentGUI:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1000x600")

        # ===== MAIN FRAME =====
        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Split into left (form) and right (table)
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side="left", fill="y", padx=10)

        right_frame = tk.Frame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True)

        # ===== FORM =====
        tk.Label(left_frame, text="Roll").grid(row=0, column=0, sticky="w")
        tk.Label(left_frame, text="Name").grid(row=1, column=0, sticky="w")
        tk.Label(left_frame, text="Course").grid(row=2, column=0, sticky="w")
        tk.Label(left_frame, text="Marks").grid(row=3, column=0, sticky="w")
        tk.Label(left_frame, text="Attendance").grid(row=4, column=0, sticky="w")

        self.roll = tk.Entry(left_frame)
        self.name = tk.Entry(left_frame)
        self.course = tk.Entry(left_frame)
        self.marks = tk.Entry(left_frame)
        self.attendance = tk.Entry(left_frame)

        self.roll.grid(row=0, column=1, pady=5)
        self.name.grid(row=1, column=1, pady=5)
        self.course.grid(row=2, column=1, pady=5)
        self.marks.grid(row=3, column=1, pady=5)
        self.attendance.grid(row=4, column=1, pady=5)

        # Buttons
        tk.Button(left_frame, text="Add", command=self.add_student).grid(row=5, column=0, pady=10)
        tk.Button(left_frame, text="Delete", command=self.delete_student).grid(row=5, column=1)
        tk.Button(left_frame, text="Update", command=self.update_student).grid(row=6, column=0, columnspan=2)
        tk.Button(left_frame, text="Clear", command=self.clear_fields).grid(row=7, column=0, columnspan=2)

        # ===== SEARCH =====
        search_frame = tk.Frame(right_frame)
        search_frame.pack(fill="x")

        tk.Label(search_frame, text="Search (Name):").pack(side="left")
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side="left", padx=5)

        tk.Button(search_frame, text="Search", command=self.search_student).pack(side="left")
        tk.Button(search_frame, text="Show All", command=self.load_data).pack(side="left")

        # ===== TABLE =====
        self.tree = ttk.Treeview(
            right_frame,
            columns=("Roll", "Name", "Course", "Marks", "Attendance"),
            show="headings"
        )

        for col in ("Roll", "Name", "Course", "Marks", "Attendance"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", stretch=True)

        self.tree.pack(fill="both", expand=True)

        # Click event
        self.tree.bind("<ButtonRelease-1>", self.select_student)

        self.load_data()

    # ===== FUNCTIONS =====

    def add_student(self):
        try:
            student = Student(
                int(self.roll.get()),
                self.name.get(),
                self.course.get(),
                int(self.marks.get()),
                int(self.attendance.get())
            )
            self.db.add_student(student)
            self.load_data()
            self.clear_fields()
        except:
            messagebox.showerror("Error", "Invalid input")

    def delete_student(self):
        try:
            self.db.delete_student(int(self.roll.get()))
            self.load_data()
            self.clear_fields()
        except:
            messagebox.showerror("Error", "Enter valid Roll Number")

    def update_student(self):
        try:
            student = Student(
                int(self.roll.get()),
                self.name.get(),
                self.course.get(),
                int(self.marks.get()),
                int(self.attendance.get())
            )
            self.db.update_student(student)
            self.load_data()
            self.clear_fields()
        except:
            messagebox.showerror("Error", "Invalid input")

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in self.db.get_students():
            self.tree.insert("", tk.END, values=row)

    def search_student(self):
        keyword = self.search_entry.get().lower()

        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in self.db.get_students():
            if keyword in row[1].lower():
                self.tree.insert("", tk.END, values=row)

    def select_student(self, event):
        selected = self.tree.focus()
        values = self.tree.item(selected, "values")

        if values:
            self.roll.delete(0, tk.END)
            self.roll.insert(0, values[0])

            self.name.delete(0, tk.END)
            self.name.insert(0, values[1])

            self.course.delete(0, tk.END)
            self.course.insert(0, values[2])

            self.marks.delete(0, tk.END)
            self.marks.insert(0, values[3])

            self.attendance.delete(0, tk.END)
            self.attendance.insert(0, values[4])

    def clear_fields(self):
        self.roll.delete(0, tk.END)
        self.name.delete(0, tk.END)
        self.course.delete(0, tk.END)
        self.marks.delete(0, tk.END)
        self.attendance.delete(0, tk.END)