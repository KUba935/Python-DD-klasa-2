import sqlite3

conn = sqlite3.connect('SQlite')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS uzytkownicy(
        id int PRIMARY KEY, 
        imie varchar(20) NOT NULL, 
        nazwisko varchar(50) NOT NULL,
        wiek int(2) NOT NULL
    )
''')

def managerAdd(name, surname, age):
    cursor = conn.cursor()

    try:
        cursor.execute('''
        INSERT INTO uzytkownicy (imie, nazwisko, wiek) VALUES (?, ?, ?)''', (name, surname, age))
    except sqlite3.Error as e:
        print(f" Błąd: {e}")
    finally:
        if conn:
            conn.close

def managerEdit(action, arg, id):
    cursor = conn.cursor()

    if action == "wiek" or "age":
        try:
            cursor.execute('''
            UPDATE uzytkownicy (
                SET wiek = ? WHERE id = ?
            )''', (arg, id))
        except sqlite3.Error as e:
            print(f" Błąd: {e}")
        finally:
            if conn:
                conn.close

    if action == "imie" or "name":
        try:
            cursor.execute('''
            UPDATE uzytkownicy (
                SET imie = ? WHERE id = ?
            )''', (arg, id))
        except sqlite3.Error as e:
            print(f" Błąd: {e}")
        finally:
            if conn:
                conn.close

    if action == "nazwisko" or "nazwisko":
        try:
            cursor.execute('''
            UPDATE uzytkownicy (
                SET wiek = ? WHERE id = ?
            )''', (arg, id))
        except sqlite3.Error as e:
            print(f" Błąd: {e}")
        finally:
            if conn:
                conn.close

def managerShow(id):
    try:
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM uzytkownicy
    ''')
        row = cursor.fetchall()

        for line in row:
            print(line)
    except sqlite3.Error as e:
        print(f" Błąd: {e}")
    finally:
        if conn:
            conn.close

def managerDelete(id):
    try:
        cursor = conn.cursor()

        row = cursor.execute('''
        DELETE FROM uzytkownicy WHERE ID = ?
    ''', id)
    except sqlite3.Error as e:
        print(f" Błąd: {e}")
    finally:
        if conn:
            conn.close

managerAdd('Roman', 'Reigns', 41)
managerAdd('Seth', 'Rollins', 40)
managerShow(1)
managerShow(2)
