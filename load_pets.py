import sqlite3
import sys

persons = (
    (1, "James", "Smith", 41),
    (2, "Diana", "Greene", 23),
    (3, "Sara", "White", 27),
    (4, "William", "Gibson", 23),
)

pets = (
    (1, "Rusty", "Dalmation", 4, 1),
    (2, "Bella", "Alaskan Malamute", 3, 0),
    (3, "Max", "Cocker Spaniel", 1, 0),
    (4, "Rocky", "Beagle", 7, 0),
    (5, "Rufus", "Cocker Spaniel", 1, 0),
    (6, "Spot", "Bloodhound", 2, 1),
)

persons_pets = ((1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6))

con = None

try:

    con = sqlite3.connect("pets.db")
    cur = con.cursor()

    with con:

        cur.execute("DROP TABLE IF EXISTS person;")
        cur.execute("DROP TABLE IF EXISTS pet;")
        cur.execute("DROP TABLE IF EXISTS person_pet;")
        cur.execute(
            "CREATE TABLE person (id INTEGER PRIMARY KEY, first_name TEXT,\
                last_name TEXT, age INTEGER)"
        )
        cur.execute(
            "CREATE TABLE pet (id INTEGER PRIMARY KEY, name TEXT, breed TEXT,\
                age INTEGER, dead INTEGER)"
        )
        cur.execute(
            "CREATE TABLE person_pet (person_id INTEGER, pet_id INTEGER)"
        )

        cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", persons)
        cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pets)
        cur.executemany("INSERT INTO person_pet VALUES(?, ?)", persons_pets)

        con.commit()
except sqlite3.Error as e:

    if con:
        con.rollback()

    print(f"Error {e.args[0]}")
    sys.exit(1)

finally:
    if cur:
        cur.close()
    if con:
        con.close()


if __name__ == "__main__":
    pass
