def faktorial(n):
    if n == 1:
            return 1
    else:
          return n * faktorial(n-1)
    

def faktorial_for(n):
      vysledek = 1
      for n in range(1, n+1):
           vysledek = vysledek * n 
      return vysledek

if __name__ == "__main__":
    print(faktorial(5))
    print (faktorial_for(5))
    