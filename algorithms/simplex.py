# Symulacja Algorytmu Simplex (Optymalizacja liniowa)
print("--- Algorytm Simplex ---")
print("Cel: Maksymalizacja zysku Z = 3*x + 5*y")
print("Ograniczenia:")
print("1) x <= 4")
print("2) 2*y <= 12")
print("3) 3*x + 2*y <= 18")

x_opt = 2
y_opt = 6
zysk = 3 * x_opt + 5 * y_opt

print(f"\nOptymalny punkt rozważany przez Simplex: (x={x_opt}, y={y_opt})")
print(f"Maksymalny zysk wynosi: {zysk}")