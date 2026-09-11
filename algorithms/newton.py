# Metoda Newtona-Raphsona - wyznaczanie pierwiastka kwadratowego
def newton_sqrt(n, iterations=10):
    x = float(n)
    for i in range(iterations):
        x = 0.5 * (x + n / x)
    return x

liczba = 25
wynik = newton_sqrt(liczba)
print(f"Obliczanie pierwiastka z {liczba}:")
print(f"Wynik: {wynik}")