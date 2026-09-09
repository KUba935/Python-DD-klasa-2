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

    return sum(1 for znak in tekst if znak samogloski)
