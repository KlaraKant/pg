def levensteinova_vzdalenost(dotaz1, dotaz2):
    """
    Levensteinova vzdalenost říka, jak jsou 2 řetězce rozdílné, pokud jsou stejné je Levensteinova vzdalenost 0,
    pro řetězce "čas" a "čaj" je Levensteinova vzdalenost 1 (liší se v 1 písmenu)
    """
    i = 0
    length = min(len(dotaz1), len(dotaz2))
    vysledek = 0
    while i < length: 
        if dotaz1[i] != dotaz2[i]:
            vysledek += 1
        i += 1
    vysledek += abs(len(dotaz1) - len(dotaz2))
    return vysledek 



def levensteinova_vzdalenost_for(dotaz1, dotaz2):
    

    pass


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam" 
    query4 = "seznam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))

    print(levensteinova_vzdalenost(query1, query4))