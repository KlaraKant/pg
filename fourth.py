def je_tah_mozny(figurka, cil_pozice, obsazeno):
    v_hranici = 1 <= cil_pozice[0] <= 8 and 1 <= cil_pozice[1] <= 8
    je_volna = cil_pozice not in obsazeno
    podminka3, podminka4 = True, True

    radek, sloupec = figurka["pozice"]
    cil_radek, cil_sloupec = cil_pozice

    if figurka["typ"] == "pěšec":
        max_kroky = 2 if radek == 2 else 1
        podminka3 = radek < cil_radek <= radek + max_kroky and sloupec == cil_sloupec
        for r in range(radek + 1, cil_radek):
            if (r, sloupec) in obsazeno:
                podminka4 = False

    elif figurka["typ"] == "jezdec":
        osa1, osa2 = abs(cil_radek - radek), abs(cil_sloupec - sloupec)
        podminka3 = (osa1, osa2) in [(2, 1), (1, 2)]

    elif figurka["typ"] == "dáma":
        if radek == cil_radek or sloupec == cil_sloupec or abs(cil_radek - radek) == abs(cil_sloupec - sloupec):
            podminka3 = True
            for r in range(min(radek, cil_radek) + 1, max(radek, cil_radek)):
                for s in range(min(sloupec, cil_sloupec) + 1, max(sloupec, cil_sloupec)):
                    if (r, s) in obsazeno:
                        podminka4 = False

    elif figurka["typ"] == "věž":
        if radek == cil_radek or sloupec == cil_sloupec:
            podminka3 = True
            for r in range(min(radek, cil_radek) + 1, max(radek, cil_radek)):
                if (r, sloupec) in obsazeno:
                    podminka4 = False
            for s in range(min(sloupec, cil_sloupec) + 1, max(sloupec, cil_sloupec)):
                if (radek, s) in obsazeno:
                    podminka4 = False

    elif figurka["typ"] == "král":
        podminka3 = abs(cil_radek - radek) <= 1 and abs(cil_sloupec - sloupec) <= 1

    elif figurka["typ"] == "střelec":
        if abs(cil_radek - radek) == abs(cil_sloupec - sloupec):
            podminka3 = True
            for r, s in zip(range(min(radek, cil_radek) + 1, max(radek, cil_radek)),
                            range(min(sloupec, cil_sloupec) + 1, max(sloupec, cil_sloupec))):
                if (r, s) in obsazeno:
                    podminka4 = False

    return f"Tah figurkou {figurka['typ']} z pozice {figurka['pozice']} na pozici {cil_pozice} je {v_hranici and je_volna and podminka3 and podminka4}"


if __name__ == "__main__":
    jezdec = {"typ": "jezdec", "pozice": (4, 5)}
    vez = {"typ": "věž", "pozice": (7, 7)}
    strelec = {"typ": "střelec", "pozice": (5, 2)}
    dama = {"typ": "dáma", "pozice": (6, 4)}
    kral = {"typ": "král", "pozice": (2, 5)}
    pesec = {"typ": "pěšec", "pozice": (3, 3)}
    obsazeno = {(3, 3), (7, 2), (4, 5), (6, 6), (6, 4), (7, 7), (5, 2), (2, 5)}

    print(je_tah_mozny(pesec, (4, 3), obsazeno))
    print(je_tah_mozny(pesec, (5, 3), obsazeno))
    print(je_tah_mozny(pesec, (6, 3), obsazeno))
    print(je_tah_mozny(pesec, (2, 3), obsazeno))
    print(je_tah_mozny(jezdec, (6, 6), obsazeno))
    print(je_tah_mozny(jezdec, (3, 6), obsazeno))
    print(je_tah_mozny(jezdec, (2, 3), obsazeno))
    print(je_tah_mozny(jezdec, (10, 5), obsazeno))
    print(je_tah_mozny(dama, (6, 1), obsazeno))
    print(je_tah_mozny(dama, (2, 4), obsazeno))
    print(je_tah_mozny(dama, (4, 7), obsazeno))