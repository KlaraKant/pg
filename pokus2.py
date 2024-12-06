from abc import ABC, abstractmethod

class Figurka(ABC):
    def __innit__(self, pozice):
        self.pozice = pozice 
    @abstractmethod
    def je_pohyb_mozny(self, nova_pozice):
        pass

class Pesak(Figurka):
    def je_pohyb_mozny(self, nova_pozice):
        if self.pozice[1] != nova_pozice[1]:
            return False
        if self.pozice[0] == 2 and nova_pozice[0] - self.pozice[0] <= 2:
            return True
        if nova_pozice[0] - self.pozice[0] == 1:
            return True
        return False
    
class Strelec(Figurka):
    def je_pohyb_mozny(self, nova_pozice):
        return True 

if __name__ == "__main__":
    figurka = Pesak((2,2))