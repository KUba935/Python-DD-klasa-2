def fahrenheity(temperatura: float):
    przelicznik =(temperatura * 1.8) + 32
    return przelicznik

def parzystosc(number: int):
    if number % 2 == 0:
        return True
    else:
        return False

def powitanie(name: str):
    zwrot = "Cześć"
    return zwrot ," ", name, "!"

def min_max(liczby):
    return min(liczby), max(liczby)

print(min_max([1, 3, 6, 3, 9]))

def samogloski(tekst):
    samogloski = "aeiouyAEIOUY"

    return sum(1 for znak in tekst if znak in samogloski)
    
def filtry(numery):
    return [num for num in numery if num = 0]

def kalkulator(cena, rabat):
    if cena < 0 or not (0 <= rabat <= 100):
        return None
    cena_koncowa = cena * (1 - rabat / 100)
    return round(cena_koncowa, 2)

def statystyki_ciagu(tekscik):
    liczba_znakow = len(tekscik)
    liczba_slow = len(tekscik.split()) if tekscik.strip() else 0
    liczba_spacji = tekscik.count(' ')
    
    return {
        "liczba_znakow": liczba_znakow,
        "liczba_slow": liczba_slow,
        "liczba_spacji": liczba_spacji
    }
