from models.animal_exotico import AnimalExotico

class BoaConstrictor(AnimalExotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.ratones_comidos = 0
    
    def hacer_sonido(self):
        return "Tsss!!"
    
    def comer_raton(self):
        if self.ratones_comidos >=20: # Cambio: Límite ahora es 20 ratones
            raise ValueError("Demasiados Ratones!!")
        self.ratones_comidos += 1