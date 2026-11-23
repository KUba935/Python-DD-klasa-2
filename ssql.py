import sqlite3

conn = sqlite3.connect('SQLlite')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Uzytkownicy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    wiek INTEGER
)
""")

while True:
    print("1. Dodaj")
    print("2. Wyświetl")
    print("3. Zmień wiek")
    print("4. Usuń")
    print("5. Zakończ")

    wybor = input("Wybierz opcję: ")
    if wybor == "1":
        imie = input("Imię: ")
        nazwisko = input("Nazwisko: ")
        wiek = int(input("Wiek: "))

        cursor.execute(
            "INSERT INTO Uzytkownicy (imie, nazwisko, wiek) VALUES (?, ?, ?)",
            (imie, nazwisko, wiek)
        )
        conn.commit()
        print("Dodano użytkownika.")

    elif wybor == "2":
        rekordy = cursor.execute(
            "SELECT id, imie, nazwisko, wiek FROM Uzytkownicy"
        ).fetchall()

        if len(rekordy) == 0:
            print("Brak użytkowników.")
        else:
            for rekord in rekordy:
                print(rekord)

    elif wybor == "3":
        id = int(input("ID użytkownika: "))
        wiek = int(input("Podaj nowy wiek: "))
        cursor.execute(
            "UPDATE Uzytkownicy SET wiek = ? WHERE id = ?",
            (wiek, id)
        )
        conn.commit()
        print("Wiek zaaktualizowany.")

    elif wybor == "4":
        id = int(input("ID użytkownika: "))
        cursor.execute(
            "DELETE FROM Uzytkownicy WHERE id = ?",
            (id,)
        )
        conn.commit()
        print("Usunięto użytkownika.")

    elif wybor == "5":
        break

cursor.close()
