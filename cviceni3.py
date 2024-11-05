def vrat_treti(seznam):
    if len(seznam)>=3:
        return seznam[2]
    else: 
        return(None)
    
def udelej_prumer(cisla):
    return sum(cisla)/len(cisla) 

def naformatuj_text(student):
    jm = student["jmeno"]
    zn = student["znamky"]
    prumer=sum(zn)/len(zn)
    print(f"Jmeno: {jm}, prumer znamek je {prumer} ")

if __name__ == "__main__":
    #patří k první funkci
    #polozky = [1,2]
    #vysledek = vrat_treti(polozky)
    #print(vysledek)

    #patří k druhé funkci
    #seznam_cisel = [1,2,10,15]
    #prumer = udelej_prumer(seznam_cisel)
    #print(prumer)

    #patří ke třetí funkci
    data = {
        "jmeno": "Bob",
        "znamky":[1,2,1,1,2,3]   
    }
    naformatuj_text(data)