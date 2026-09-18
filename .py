# Zadanie 1
def fahrenheity(temperatura: float):
    przelicznik =(temperatura * 1.8) + 32
    return przelicznik
# Zadanie 2 
def parzystosc(number: int):
    if number % 2 == 0:
        return True
    else:
        return False
# Zadanie 3
def powitanie(name: str):
    zwrot = "Cześć"
    return zwrot ," ", name, "!"
# Zadanie 4
def min_max(liczby):
    return min(liczby), max(liczby)

print(min_max([1, 3, 6, 3, 9]))
# Zadanie 5
def samogloski(tekst):
    samogloski = "aeiouyAEIOUY"

    return sum(1 for znak in tekst if znak in samogloski)
# Zadanie 6
def filtry(numery):
    return [num for num in numery if num = 0]
# Zadanie 7
def kalkulator(cena, rabat):
    if cena < 0 or not (0 <= rabat <= 100):
        return None
    cena_koncowa = cena * (1 - rabat / 100)
    return round(cena_koncowa, 2)
# Zadanie 8
def statystyki_ciagu(tekscik):
    liczba_znakow = len(tekscik)
    liczba_slow = len(tekscik.split()) if tekscik.strip() else 0
    liczba_spacji = tekscik.count(' ')
    
    return {
        "liczba_znakow": liczba_znakow,
        "liczba_slow": liczba_slow,
        "liczba_spacji": liczba_spacji
    }
# Zadanie 9
def uniwersalna_srednia(*args):
  if not args:
    return 0
  return sum(args) / len(args)
# Zadanie 10
import math

def pole_kola(promien):
    return math.pi * (promien ** 2)

def objetosc_walca(promien, wysokosc):
    pole_podstawy = pole_kola(promien)
    return pole_podstawy * wysokosc
r = 3.0
h = 5.0
wynik = objetosc_walca(r, h)
print(f"Objętość walca wynosi: {wynik:.2f}")
# Zadanie 11
