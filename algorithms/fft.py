import math

def dft(sygnal):
    N = len(sygnal)
    wyniki = []
    
    # k = numer częstotliwości (prążka)
    for k in range(N):
        suma_real = 0.0
        suma_imag = 0.0
        
        # n = kolejna próbka sygnału w czasie
        for n in range(N):
            kat = 2 * math.pi * k * n / N
            
            # Wzór Eulera: cosinus to część rzeczywista, sinus to urojona
            suma_real += sygnal[n] * math.cos(kat)
            suma_imag -= sygnal[n] * math.sin(kat)
            
        # Obliczamy moc/siłę danej częstotliwości (amplitudę)
        amplituda = math.sqrt(suma_real**2 + suma_imag**2)
        
        wyniki.append({
            "k": k,
            "real": round(suma_real, 2),
            "imag": round(suma_imag, 2),
            "amplituda": round(amplituda, 2)
        })
        
    return wyniki


sygnal = [1, 2, 1, -1]
widmo = dft(sygnal)

print("=== WYNIKI DYSKRETNEJ TRANSFORMACJI FOURIERA ===")
print("k | Część Re | Część Im | Sila (Amplituda) | Wykres mocy")
print("-" * 55)

for p in widmo:
    # Rysujemy prosty wykres z gwiazdek
    wykres = "*" * int(p["amplituda"] * 2)
    print(f"{p['k']} | {p['real']:8.2f} | {p['imag']:8.2f} | {p['amplituda']:16.2f} | {wykres}")