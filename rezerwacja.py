import sqlite3
conn = sqlite3.connect('rezerwacje.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Wydarzenia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT,
    dostepne_miejsca INTEGER
)
""")
conn.commit()

while True:
    print("SYSTEM REZERWACJI WYDARZEŃ")
    print("1. Dodaj nowe wydarzenie")
    print("2. Zarezerwuj miejsce")
    print("3. Anuluj rezerwację")
    print("4. Wyświetl dostępne wydarzenia")
    print("5. Zakończ")

    wybor = input("Wybierz opcję: ")
    
    if wybor == "1":
        nazwa_wydarzenia = input("Nazwa nowego wydarzenia: ")
        liczba_miejsc = int(input("Liczba dostępnych miejsc: "))
        
        cursor.execute(
            "INSERT INTO Wydarzenia (nazwa, dostepne_miejsca) VALUES (?, ?)",
            (nazwa_wydarzenia, liczba_miejsc)
        )
        conn.commit()
        print("Dodano nowe wydarzenie do bazy.")

    elif wybor == "2":
        id_wydarzenia = int(input("Podaj ID wydarzenia, na które chcesz się zarezerwować: "))
        
        cursor.execute("SELECT dostepne_miejsca, nazwa FROM Wydarzenia WHERE id = ?", (id_wydarzenia,))
        wynik = cursor.fetchone()
        
        if wynik is None:
            print("Nie ma wydarzenia o takim ID.")
        else:
            miejsca = wynik[0]
            nazwa = wynik[1]
            
            if miejsca > 0:
                cursor.execute(
                    "UPDATE Wydarzenia SET dostepne_miejsca = dostepne_miejsca - 1 WHERE id = ?",
                    (id_wydarzenia,)
                )
                conn.commit()
                print(f"Udało się zarezerwować miejsce na: '{nazwa}'!")
            else:
                print("Przykro nam, brak wolnych miejsc na to wydarzenie.")

    elif wybor == "3":
        id_wydarzenia = int(input("Podaj ID wydarzenia, z którego rezygnujesz: "))
        
        cursor.execute("SELECT dostepne_miejsca, nazwa FROM Wydarzenia WHERE id = ?", (id_wydarzenia,))
        wynik = cursor.fetchone()
        
        if wynik is None:
            print("Nie ma wydarzenia o takim ID.")
        else:
            nazwa = wynik[1]
            cursor.execute(
                "UPDATE Wydarzenia SET dostepne_miejsca = dostepne_miejsca + 1 WHERE id = ?",
                (id_wydarzenia,)
            )
            conn.commit()
            print(f"Anulowano rezerwację dla: '{nazwa}'. Miejsca zostały przywrócone.")

    elif wybor == "4":
        cursor.execute("SELECT id, nazwa, dostepne_miejsca FROM Wydarzenia")
        rekordy = cursor.fetchall()

        if len(rekordy) == 0:
            print("Brak wydarzeń w bazie.")
        else:
            print("LISTA WYDARZEŃ")
            for rekord in rekordy:
                print(f"ID: {rekord[0]} | Wydarzenie: {rekord[1]} | Wolne miejsca: {rekord[2]}")


    elif wybor == "5":
        print("Do zobaczenia!.")
        break

cursor.close()
conn.close()