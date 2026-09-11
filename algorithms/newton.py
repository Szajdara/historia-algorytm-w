def newton_sqrt(n, tol=1e-10):
    if n < 0:
        raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej.")
    if n == 0:
        return 0.0

    x = float(n)
    while True:
        next_x = 0.5 * (x + n / x)
        if abs(next_x - x) < tol:
            return next_x
        x = next_x

# Test
liczba = 25
print(f"Pierwiastek z {liczba}: {newton_sqrt(liczba)}")