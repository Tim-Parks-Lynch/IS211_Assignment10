import sqlite3

con = sqlite3.connect("pets.db")
name = "William"
pet = "Spot"
person_id = 4


with con:
    cur = con.cursor()
    cur.execute("SELECT * from person;")

    column_names = [cn[0] for cn in cur.description]

    rows = cur.fetchall()
    print(
        f"{column_names[0]:3} {column_names[1]:10} {column_names[2]:7} {column_names[3]:10}"
    )

    for row in rows:
        print(f"{row[0]:<4} {row[1]:<10} {row[2]:8} {row[3]:1}")

    cur.execute("SELECT * from person WHERE first_name=?", (name,))

    column_name = [cn[0] for cn in cur.description]

    rows = cur.fetchall()
    print(
        f"{column_name[0]:3} {column_name[1]:10} {column_name[2]:7} {column_name[3]:10}"
    )

    for row in rows:
        print(f"{row[0]:<4} {row[1]:<10} {row[2]:8} {row[3]:1}")

if __name__ == "__main__":
    pass
