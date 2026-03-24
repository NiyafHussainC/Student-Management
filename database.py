import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll INTEGER PRIMARY KEY,
            name TEXT,
            course TEXT,
            marks INTEGER,
            attendance INTEGER
        )
        """)
        self.conn.commit()

    def add_student(self, student):
        self.cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (
            student.get_roll(),
            student.get_name(),
            student.get_course(),
            student.get_marks(),
            student.get_attendance()
        ))
        self.conn.commit()

    def get_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def delete_student(self, roll):
        self.cursor.execute("DELETE FROM students WHERE roll=?", (roll,))
        self.conn.commit()

    def update_student(self, student):
        self.cursor.execute("""
        UPDATE students 
        SET name=?, course=?, marks=?, attendance=? 
        WHERE roll=?
        """, (
            student.get_name(),
            student.get_course(),
            student.get_marks(),
            student.get_attendance(),
            student.get_roll()
        ))
        self.conn.commit()