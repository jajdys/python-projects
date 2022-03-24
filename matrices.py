import numpy as np

x = input("Kolumna: ")
y = input("Wiersz: ")
x = int(x)
y = int(y)
matrices_1 = np.random.randint(100, size=(x, y))
print("Macierz 1: \n", matrices_1)

a = input("Kolumna: ")
b = input("Wiersz: ")
a = int(a)
b = int(b)
matrices_2 = np.random.randint(100, size=(a, b))
print("Macierz 1: \n", matrices_2)
print("\n")

matrices_3 = matrices_1 + matrices_2
print("Dodawanie macierzy")
print(matrices_3)
print("\n")
matrices_4 = matrices_1 * matrices_2
print("Mnozenie macierzy")
print(matrices_4)
print("\n")