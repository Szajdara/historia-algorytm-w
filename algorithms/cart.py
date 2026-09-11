class Node:
    def __init__(self, cecha=None, prog=None, lewy=None, prawy=None, decyzja=None):
        self.cecha = cecha      # Nazwa cechy (np. 'wiek')
        self.prog = prog        # Wartość podziału (np. 30)
        self.lewy = lewy        # Dziecko, gdy warunek spełniony (<= prog)
        self.prawy = prawy      # Dziecko, gdy warunek niespełniony (> prog)
        self.decyzja = decyzja  # Wynik (tylko w liściach)

def przewiduj(wezel, dane):
    """Rekurencyjnie przechodzi po drzewie do momentu trafienia na decyzję."""
    if wezel.decyzja is not None:
        return wezel.decyzja

    wartosc = dane[wezel.cecha]
    if wartosc <= wezel.prog:
        return przewiduj(wezel.lewy, dane)
    else:
        return przewiduj(wezel.prawy, dane)

drzewo = Node(
    cecha="wiek", prog=30,
    lewy=Node(decyzja="Grupa A: Młody użytkownik"),
    prawy=Node(
        cecha="dochod", prog=5000,
        lewy=Node(decyzja="Grupa C: Standardowe dochody"),
        prawy=Node(decyzja="Grupa B: Wysokie dochody")
    )
)

osoba1 = {"wiek": 25, "dochod": 3000}
osoba2 = {"wiek": 42, "dochod": 7500}

print("Osoba 1:", przewiduj(drzewo, osoba1))
print("Osoba 2:", przewiduj(drzewo, osoba2))