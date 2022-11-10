from helper_functions import try_connection
import sqlite3

PERSON_QRY = "SELECT * FROM person WHERE id=?;"
PERSON_PET_QUERY = "SELECT p.first_name, p.last_name, pt.name, pt.breed, \
    pt.age, pt.dead FROM person p INNER JOIN person_pet pp \
        ON p.id = pp.person_id INNER JOIN pet pt ON pt.id = pp.pet_id \
            WHERE pp.person_id=?"


def main(db_name):

    if try_connection(db_name):
        con = sqlite3.connect(db_name)
        cur = con.cursor()

        while True:
            user_input = input("\nID of pet owner ")

            if user_input <= "0":
                print("Exiting program")
                break
            else:
                id = int(user_input)
                with con:
                    cur.execute(PERSON_QRY, (id,))
                    row = cur.fetchone()
                    if row:

                        print("\n" f"{row[1]} {row[2]} is {row[3]} years old.")
                        cur.execute(
                            PERSON_PET_QUERY, (id,)
                        )  # for pets and owners
                        for row in cur.fetchall():
                            if row[5]:
                                print(
                                    f"{row[0]} {row[1]} owned {row[2]}, a "
                                    f"{row[3]}, that was {row[4]} years old."
                                )
                            else:
                                print(
                                    f"{row[0]} {row[1]} owns {row[2]}, a "
                                    f"{row[3]}, that is {row[4]} years old."
                                )
                    else:
                        print("\nNo pet owner found")
                        print("Enter -1 in pet owner field to exit program")


if __name__ == "__main__":
    main("pets.db")
