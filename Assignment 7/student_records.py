import sqlite3

conn = sqlite3.connect("StudentRecords.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS StudentRecords")

cursor.execute("""
CREATE TABLE StudentRecords (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Age INTEGER,
    Major TEXT NOT NULL
)
""")
cursor.execute(
    "INSERT INTO StudentRecords (ID, Name, Age, Major) VALUES (?, ?, ?, ?)",
    (1, "Alex", 20, "Biology")
)
cursor.execute(
    "INSERT INTO StudentRecords (ID, Name, Age, Major) VALUES (?, ?, ?, ?)",
    (2, "Ty", 30, "Business")
)
cursor.execute(
    "INSERT INTO StudentRecords (ID, Name, Age, Major) VALUES (?, ?, ?, ?)",
    (3, "Fiona", 19, "Nursing")
)
cursor.execute(
    "INSERT INTO StudentRecords (ID, Name, Age, Major) VALUES (?, ?, ?, ?)",
    (4, "Jasmine", 26, "Kinesiology")
)
cursor.execute(
    "INSERT INTO StudentRecords (ID, Name, Age, Major) VALUES (?, ?, ?, ?)",
    (5, "David", 57, "Accounting")
)

cursor.execute("SELECT Name, Age, Major FROM StudentRecords")

students = cursor.fetchall()

for student in students:
    print(student)

answer = input("Do you want to add a new student? (yes/no): ").strip().lower()

while answer != "yes" and answer != "no":
    answer = input("Please enter yes or no: ").strip().lower()

if answer == "yes":
    name = input("Enter the student's name: ").strip()

    while not name:
        name = input("Name cannot be empty. Enter the student's name: ").strip()
    while True:
            age = input("Enter the student's age: ").strip()
            try:
                age = int(age)
                if age >= 0:
                    break
                print("Please enter a whole number.")
            except ValueError:
                print("Please enter a whole number.")
    major = input("Enter the student's major: ").strip()
    while not major:
     major = input("Major cannot be empty. Enter the student's major: ").strip()
    cursor.execute("SELECT MAX(ID) FROM StudentRecords")
    new_id = cursor.fetchone()[0] + 1
    cursor.execute(
    "INSERT INTO StudentRecords (ID, Name, Age, Major) VALUES (?, ?, ?, ?)",
    (new_id, name, age, major)
)
conn.commit()
conn.close()
