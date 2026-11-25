import sqlite3

conn = sqlite3.connect('biblioteka.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Biblioteka (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tytul TEXT,
    autor TEXT
)
""")
conn.commit()

while True:
    print("SYSTEM BIBLIOTEKI")
    print("1. Dodaj")
    print("2. Usuń")
    print("3. Zaaktualizuj")
    print("4. Wyświetl")
    print("5. Zakończ")

    wybor = input("Wybierz opcję: ")
    
    if wybor == "1":
        tytul = input("Tytuł: ")
        autor = input("Autor: ")
        cursor.execute(
            "INSERT INTO Biblioteka (tytul, autor) VALUES (?, ?)",
            (tytul, autor)
        )
        conn.commit()
        print("Dodano książkę.")
         
    elif wybor == "2":
        id_ksiazki = int(input("ID książki do usunięcia: "))
        cursor.execute(
            "DELETE FROM Biblioteka WHERE id = ?",
            (id_ksiazki,)
        )
        conn.commit()
        print("Usunięto książkę.")

    elif wybor == "3":
        id_ksiazki = int(input("ID książki do aktualizacji: "))
        nowy_tytul = input("Podaj nowy tytuł: ")
        
        cursor.execute(
            "UPDATE Biblioteka SET tytul = ? WHERE id = ?",
            (nowy_tytul, id_ksiazki)
        )
        conn.commit()
        print("Zaktualizowano.")

    elif wybor == "4":
        cursor.execute("SELECT id, tytul, autor FROM Biblioteka")
        rekordy = cursor.fetchall()

        if len(rekordy) == 0:
            print("Brak książek w bazie.")
        else:
            print("\n--- LISTA KSIĄŻEK Z BAZY ---")
            for rekord in rekordy:
                print(f"ID: {rekord[0]} | Tytuł: {rekord[1]} | Autor: {rekord[2]}")

    elif wybor == "5":
        print("Do zobaczenia!")
        break

cursor.close()
conn.close()