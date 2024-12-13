# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte třídu `Shape` s abstraktní metodou `area`.
# Vytvořte dvě podtřídy: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

from abc import ABC, abstractmethod

pí = 3.14159

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape): #nová třída, která dědí z Shape
    def __init__(self, width, height): #má argumenty width, height 
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height #výpočet obsahu obdélníku, vrací obsah obdélníku 

class Circle(Shape): # nová třída, která dědí z Shape
    def __init__(self, radius): #má argumenty radius
        self.radius = radius

    def area(self):
        return pí*self.radius**2  #používá konstantu pí, kterou jsem definovala nahoře, vrací průměr kruhu 

from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 2) == 28.27

    with patch("abc.ABC", side_effect=NotImplementedError):
        try:
            shape = Shape()
        except TypeError:
            pass