
import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS books")

cursor.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    genre TEXT,
    copies INTEGER,
    rating INTEGER
)
""")

cursor.execute("""
INSERT INTO books (title, author, year, genre, copies, rating)
VALUES (?, ?, ?, ?, ?, ?)
""", ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 4, 5))

books = [
    ("Dune", "Frank Herbert", 1965, "Science Fiction", 3, 5),
    ("The Silent Patient", "Alex Michaelides", 2019, "Mystery", 2, 4),
    ("A Brief History of Time", "Stephen Hawking", 1988, "Science", 3, None),
    ("The Diary of a Young Girl", "Anne Frank", 1947, "History", 2, 5),
    ("Pride and Prejudice", "Jane Austen", 1813, "Romance", 5, None),
    ("The Martian", "Andy Weir", 2011, "Science", 4, 5),
    ("Sherlock Holmes", "Arthur Conan Doyle", 1892, "Mystery", 1, 4)
]

cursor.executemany("""
INSERT INTO books (title, author, year, genre, copies, rating)
VALUES (?, ?, ?, ?, ?, ?)
""", books)

conn.commit()

print("\nBooks published after 1990:")
cursor.execute("SELECT title, author FROM books WHERE year > 1990")
for row in cursor.fetchall():
    print(row)

print("\nFiction books with more than 2 copies:")
cursor.execute("SELECT title FROM books WHERE genre != 'Science' AND copies > 2")
for row in cursor.fetchall():
    print(row)

print("\nBooks published before 1900 or rated 5:")
cursor.execute("SELECT title FROM books WHERE year < 1900 OR rating = 5")
for row in cursor.fetchall():
    print(row)

print("\nBooks not in the Mystery genre:")
cursor.execute("SELECT title FROM books WHERE NOT genre = 'Mystery'")
for row in cursor.fetchall():
    print(row)

print("\nBooks in the Science or History genre:")
cursor.execute("SELECT title FROM books WHERE genre IN ('Science', 'History')")
for row in cursor.fetchall():
    print(row)

letter = input("\nEnter a letter to search for authors: ").strip()

print(f"\nAuthors whose names start with {letter}:")
cursor.execute("SELECT author FROM books WHERE author LIKE ?", (letter + "%",))
for row in cursor.fetchall():
    print(row)

print("\nBooks with no rating:")
cursor.execute("SELECT title FROM books WHERE rating IS NULL")
for row in cursor.fetchall():
    print(row)

conn.close()

