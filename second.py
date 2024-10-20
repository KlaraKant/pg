def cislo_text(cislo):
    cislo = int(cislo)

    if cislo == 0:
        return("Nula")

    if cislo == 100:
        return("Sto")
    
    if cislo > 1 and cislo < 11:
        jednotky = {1: "Jedna", 2: "Dva", 3: "Tři", 4: "Čtyři", 5: "Pět", 6: "Šest", 7: "Sedm", 8: "Osm", 9: "Devět", 10: "Deset"}
        return jednotky[cislo]
    
    if cislo > 10 and cislo < 20:
        desitky_nact = {11: "Jedenáct", 12: "Dvanáct", 13: "Třináct", 14:"Čtrnáct", 15: "Patnáct", 16: "Šestnáct", 17: "Sedmnáct", 18:"Osmnáct", 19: "Devatenáct"}
        return desitky_nact[cislo]
    
    if cislo >= 20 and cislo < 100:
        desitky = {2: "Dvacet", 3: "Třicet", 4: "Čtyřicet", 5: "Padesát", 6: "Šedesát", 7: "Sedmdesát", 8: "Osmdesát", 9: "Devadesát"}
        jednotky_k_desitce = {1: "jedna", 2: "dva", 3: "tři", 4: "čtyři", 5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět"}
        
        bez_zbytku = cislo // 10 
        se_zbytkem = cislo % 10
        
        if se_zbytkem == 0:
            return desitky[bez_zbytku]
        else:
            return desitky[bez_zbytku] + " " + jednotky_k_desitce[se_zbytkem]


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)