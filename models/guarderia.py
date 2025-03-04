from models.huron import Huron
from models.boa_constrictor import BoaConstrictor

class Guarderia:
    def __init__(self):
        self.boas =[
            BoaConstrictor(nombre="Sonia", peso=15.0, edad=5, pais_origen="Brasil", impuestos=1.5),
            BoaConstrictor(nombre="Maria", peso=12.0, edad=5, pais_origen="Peru", impuestos=1.3)
        ]

        self.hurones =[
            Huron(nombre="Paco", peso=2.5, edad=3, pais_origen="España", impuestos=1.2),
            Huron(nombre="Raul", peso=3.0, edad=2, pais_origen="Francia", impuestos=1.1)
        ]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta boa no existe!"
        try:
            boa.comer_raton()
            return "Exito!!"
        except ValueError:
            return "La boa esta llena!"