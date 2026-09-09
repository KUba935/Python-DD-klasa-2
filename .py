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