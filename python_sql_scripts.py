# For me only - do not run this file
# ---------------------PYTHON_SQL SCRIPTS -------------------- #
# URL FOR MORE INFO https://zetcode.com/python/sqlite/
# CREATE TABLE and LOAD VALUES

# import sqlite3
# import sys

# persons = (
#     (1, "James", "Smith", 41),
#     (2, "Diana", "Greene", 23),
#     (3, "Sara", "White", 27),
#     (4, "William", "Gibson", 23),
# )

# pets = (
#     (1, "Rusty", "Dalmation", 4, 1),
#     (2, "Bella", "Alaskan Malamute", 3, 0),
#     (3, "Max", "Cocker Spaniel", 1, 0),
#     (4, "Rocky", "Beagle", 7, 0),
#     (5, "Rufus", "Cocker Spaniel", 1, 0),
#     (6, "Spot", "Bloodhound", 2, 1),
# )

# person_pet = ((1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6))

# con = None

# try:

#     con = sqlite3.connect("pets.db")

#     with con:
#         cur = con.cursor()

#         cur.execute("DROP TABLE IF EXISTS person;")
#         cur.execute("DROP TABLE IF EXISTS pet;")
#         cur.execute("DROP TABLE IF EXISTS person_pet;")
#         cur.execute(
#             "CREATE TABLE person (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)"
#         )
#         cur.execute(
#             "CREATE TABLE pet (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)"
#         )
#         cur.execute(
#             "CREATE TABLE person_pet (person_id INTEGER, pet_id INTEGER)"
#         )

#         cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", persons)
#         cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pets)
#         cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)

#         con.commit()
# except sqlite3.Error as e:

#     if con:
#         con.rollback()

#     print(f"Error {e.args[0]}")
#     sys.exit(1)

# finally:

#     if con:
#         con.close()


# ---------------------PYTHON_SQL SCRIPTS -------------------- #
# SELECT STATEMENTS

# import sqlite3

# con = sqlite3.connect("pets.db")

# with con:
#     cur = con.cursor()
#     cur.execute("SELECT * from person")

#     column_names = [cn[0] for cn in cur.description]

#     rows = cur.fetchall()
#     print(
#         f"{column_names[0]:3} {column_names[1]:10} {column_names[2]:7} {column_names[3]:10}"
#     )

#     for row in rows:
#         print(f"{row[0]:<4} {row[1]:<10} {row[2]:8} {row[3]:1}")

# Returns
# id  first_name last_name age
# 1    James      Smith    41
# 2    Diana      Greene   23
# 3    Sara       White    27
# 4    William    Gibson   23


# ---------------------PYTHON_SQL SCRIPTS -------------------- #
# SELECT STATEMENT with Parameterized Values

# import sqlite3

# name = "William"
# con = sqlite3.connect("pets.db")

# with con:
#     cur = con.cursor()
#     cur.execute("SELECT * from person WHERE first_name=?", (name,))

#     column_name = [cn[0] for cn in cur.description]

#     rows = cur.fetchall()
#     print(
#         f"{column_name[0]:3} {column_name[1]:10} {column_name[2]:7} {column_name[3]:10}"
#     )

#     for row in rows:
#         print(f"{row[0]:<4} {row[1]:<10} {row[2]:8} {row[3]:1}")

# Returns
# id  first_name last_name age
# 4    William    Gibson   23


# ---------------------PYTHON_SQL SCRIPTS -------------------- #
#
