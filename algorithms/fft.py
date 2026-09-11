# Dyskretna Transformacja Fouriera (DFT)
import math

def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        real = sum(x[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = -sum(x[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        X.append((round(real, 2), round(imag, 2)))
    return X

sygnal = [1, 2, 1, -1]
print(f"Sygnał wejściowy: {sygnal}")
print(f"Widmo częstotliwościowe (Re, Im): {dft(sygnal)}")