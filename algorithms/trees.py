# Drzewo przeszukiwań binarnych (BST)
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
    else:
        korzen.prawy = wstaw(korzen.prawy, klucz)
    return korzen

def inorder(korzen):
    return inorder(korzen.lewy) + [korzen.klucz] + inorder(korzen.prawy) if korzen else []

root = None
elementy = [20, 10, 30, 5, 15]
for x in elementy:
    root = wstaw(root, x)

print(f"Wstawiono elementy: {elementy}")
print("Porządek in-order (posortowany):", inorder(root))