biblioteka = {
    "Wiedźmin": "dostępna",
    "Pan Tadeusz": "wypożyczona",
    "Lalka": "dostępna",
}

while True:
  print("> Biblioteka")
  print("> Wybierz opcje")
  print("1 Dodaj książkę")
  print("2 Wypożycz książkę")
  print("3 Zwróć książkę")
  print("4 Wyświetl listę książek")

  wybor = input("Opcja nr : ")

  if wybor == "1":
    tytul = input("Podaj tytuł nowej książki: ")
    if tytul:
      biblioteka[tytul] = "dostępna"
      print(f"Dodano książkę '{tytul}' do biblioteki.")
    else:
      print("Błąd: Tytuł nie może być pusty!")

  elif wybor == "2":
    tytul = input("Podaj tytuł książki do wypożyczenia: ")
    if tytul in biblioteka:
      if biblioteka[tytul] == "dostępna":
        biblioteka[tytul] = "wypożyczona"
        print(f"Udało się wypożyczyć książkę: '{tytul}'.")
      else:
        print(f"Błąd: Książka '{tytul}' jest już wypożyczona!")
    else:
      print("Błąd: Nie ma takiej książki w bibliotece!")

  elif wybor == "3":
    tytul = input("Podaj tytuł książki do zwrotu: ")
    if tytul in biblioteka:
      if biblioteka[tytul] == "wypożyczona":
        biblioteka[tytul] = "dostępna"
        print(f"Przyjęto zwrot książki: '{tytul}'.")
      else:
        print(f"Błąd: Ta książka nie była wypożyczona!")
    else:
      print("Błąd: Nie ma takiej książki w bibliotece!")

  elif wybor == "4":
    print("--- LISTA KSIĄŻEK ---")
    for tytul, status in biblioteka.items():
      print(f"- {tytul} [{status}]")
    


    
  