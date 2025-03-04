import unittest
from models.boa_constrictor import BoaConstrictor


class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        self.boaC = BoaConstrictor(nombre="Sonia", peso=15.0, edad=5, pais_origen="Brasil", impuestos=1.5)

    def test_hacer_sonido(self):
        # Prueba que el sonido de la boa constrictor es correcto
        self.assertEqual(self.boaC.hacer_sonido(), "Tsss!!")

    def test_calcular_flete(self):
        # Prueba que el cálculo del flete es correcto
        flete_esperado = self.boaC.obtener_peso() * self.boaC.impuestos
        self.assertEqual(self.boaC.calcular_flete(), flete_esperado)

    def test_comer_raton(self):
        # Prueba que el conteo de ratones comidos es correcto
        self.assertEqual(self.boaC.ratones_comidos, 0)  # Inicialmente no ha comido ratones
        self.boaC.comer_raton()
        self.assertEqual(self.boaC.ratones_comidos, 1)  # Después de comer un ratón

    def test_comer_demasiados_ratones(self):
        # Prueba que ahora no se pueden comer más de 20 ratones
        for i in range(21):# Supera la cantidad de ratones permitidos, por lo que deberia dar error
            self.boaC.comer_raton()
        self.assertEqual(self.boaC.ratones_comidos, 20) # Límite de ratones comidos permitidos
        with self.assertRaises(ValueError):
            self.boaC.comer_raton()

if __name__ == "__main__":
    unittest.main()