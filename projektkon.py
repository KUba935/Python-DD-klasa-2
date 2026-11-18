from pathlib import *
path = Path("Reigns.txt")
sum = 0
wliczby = 0
if path.is_file():
    with open(path, "r", encoding="utf-8") as file:
        for liczba_line, line in enumerate(file, start=1):
            text = line.strip()
            try:
                liczba = int(text)
                wliczby += 1
                sum + text
            except ValueError:
                break
        print(f"Wynik całkowity to: {sum}")
        with open("zapis.txt", "a", encoding="utf-8") as file_save:
            file_save.write(f"Wynik całkowity to:{sum}")
else:
    print("Uwaga: Wybrany plik nie istnieje.")
    

    