class Wezel:
    def __init__(self, klucz):
        self.klucz = klucz
        self.lewy = None
        self.prawy = None

def wstaw(korzen, klucz):
    if korzen is None:
        return Wezel(klucz)
    if klucz < korzen.klucz:
        korzen.lewy = wstaw(korzen.lewy, klucz)
    elif klucz > korzen.klucz:
        korzen.prawy = wstaw(korzen.prawy, klucz)
    return korzen

def szukaj(korzen, klucz):
    """Zwraca True, jeśli klucz znajduje się w drzewie BST."""
    if korzen is None:
        return False
    if korzen.klucz == klucz:
        return True
    if klucz < korzen.klucz:
        return szukaj(korzen.lewy, klucz)
    return szukaj(korzen.prawy, klucz)

def inorder(korzen, wynik=None):
    """Przechodzenie in-order bez nadmiernej alokacji pamięci."""
    if wynik is None:
        wynik = []
    if korzen:
        inorder(korzen.lewy, wynik)
        wynik.append(korzen.klucz)
        inorder(korzen.prawy, wynik)
    return wynik

root = None
elementy = [20, 10, 30, 5, 15]
for x in elementy:
    root = wstaw(root, x)

print("Wstawiono elementy:", elementy)
print("In-order (posortowane):", inorder(root))
print("Czy 15 jest w drzewie?:", szukaj(root, 15))
print("Czy 99 jest w drzewie?:", szukaj(root, 99))