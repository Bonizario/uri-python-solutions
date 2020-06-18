x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [x[i * n:(i + 1) * n] for i in range((len(x) + n - 1) // n)]
