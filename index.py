def suma(a, b):
    return a + b
print(suma(5, 6))

def silnia(x):
    return x * (x - 1)
print(silnia(6))

def zwrot(string):
    return string[::-1]
print(zwrot("reigns"))

def pierwsza(c):

    if c == 0:
        return 0
    
    for i in range(2, 10):
        print(i)
        if c % i == 0:
            return False
        
    return True
print(pierwsza(1))

    


