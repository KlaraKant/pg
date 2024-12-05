def je_prvocislo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    try:
        cislo = int(cislo)
        print(je_prvocislo(cislo))
    except ValueError:
        print("Neplatný vstup. Zadejte prosím celé číslo.")