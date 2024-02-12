# Napisz skrypt, który wyświetla liczby parzyste z zakresu od 0 do 10
for i in range(0, 11, 2):
    print(i, end=" ")
print("\n")

# Napisz skrypt, który wypisze co czwartą liczbę z zakresu 1 do 50
for i in range(0, 51, 4):
    print(i, end=" ")
print("\n")

# Napisz skrypt, który znajdzie najmniejszą wartość na liście.
tabela = [22, 47, 53, 7, 3, 496, 974, 32, 20]
low = tabela[0]
for i in tabela:
    if i <= low:
        low = i
print(low)
print("\n")

# Napisz skrypt, który poda sumę liczby akutalnej i poprzedniej z zakresu od 0 do 10
poprzednia = 1
for i in range(1, 11):
    print(poprzednia + i, end=" ")
    poprzednia = i

