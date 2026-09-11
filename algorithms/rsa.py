# Uproszczone Szyfrowanie RSA
p, q = 3, 11
n = p * q           # Moduł n = 33
phi = (p - 1) * (q - 1) # 20
e = 3               # Wykładnik publiczny
d = 7               # Wykładnik prywatny

wiadomosc = 5
szyfrogram = (wiadomosc ** e) % n
odszyfrowana = (szyfrogram ** d) % n

print(f"Wiadomość oryginalna: {wiadomosc}")
print(f"Zaszyfrowana wiadomość (C = M^e mod n): {szyfrogram}")
print(f"Odszyfrowana wiadomość (M = C^d mod n): {odszyfrowana}")