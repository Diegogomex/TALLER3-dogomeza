import unittest
from models.huron import Huron

class testHuron(unittest.TestCase):
    def setUp (self):
        self.huron = Huron(nombre="Paco", peso=2.5, edad=3, pais_origen="España", impuestos=1.2)

    def test_hacer_sonido(self):
        # Prueba que el sonido del hurón es correcto
        self.assertEqual(self.huron.hacer_sonido(), "Eek, Eek!!")

    def test_calcular_flete(self):
        # Prueba que el cálculo del flete es correcto
        flete_esperado = self.huron.obtener_peso() * self.huron.impuestos
        self.assertEqual(self.huron.calcular_flete(), flete_esperado)

if __name__ == "__main__":
    unittest.main()