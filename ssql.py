import sqllite3

conn = sqllite3.connect('example.db')
cursor = conn.cursor()

cursor.execute( '''
    CREATE TABLE uzytkownicy
    ( id int PRIMARY KEY, 
    imie varchar(20) NOT NULL, 
    nazwisko varchar(50) NOT NULL,
     wiek int(2) NOT NULL );
''')

cursor.execute('''
INSERT INTO uzytkownicy (
(imie, nazwisko, wiek) VALUES (?, ?, ?)
);
''')