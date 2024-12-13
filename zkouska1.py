# Příklad 1: Práce s podmínkami a cykly
# Zadání:
# Napište funkci `process_numbers`, která přijme seznam celých čísel. 
# Funkce vrátí nový seznam, který obsahuje pouze čísla větší než 5, vynásobená 2.
# Pokud seznam obsahuje číslo 10, ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_numbers(numbers):
    vysledky = [] #vytváří seznam výsledky 
    for cislo in numbers: #procházení čísel v seznamu "numbers"
        if cislo == 10:
            return vysledky #pokud je číslo 10, ukončí funkci a vrátí dosud vytvořený seznam
        if cislo > 5:
            vysledky += [cislo*2] #pokud je číslo větší než 5, vynásobí 2 a zanese do seznamu 
    return vysledky #vrátí nově vytvořený seznam výsledků


def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]