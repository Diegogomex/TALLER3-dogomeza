
from models.ianimal import IAnimal

class Animal(IAnimal):
    def __init__(self, nombre, peso, edad):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0

    def comer (self, kilos):
        self._kilos_comidos += kilos

    def obtener_kilos_comidos(self):
        return self._kilos_comidos
    
    def hacer_sonido(self):
        pass
    
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_peso(self):
        return self._peso
    
    def obtener_edad(self):
        return self._edad
    
    
