from models.huron import Huron
from models.boa_constrictor import BoaConstrictor

#instancias
huron1 = Huron(nombre="Paco", peso=2.5, edad=3, pais_origen="España", impuestos=1.2)
boaC1 = BoaConstrictor (nombre="Sonia", peso=15.0, edad=5, pais_origen="Brasil", impuestos=1.5)

#Pruebas
print(f"Nombre del Huron: {huron1.obtener_nombre()}")
print(huron1.hacer_sonido())
print(f"Peso: {huron1.obtener_peso()} kg")
print(f"Edad: {huron1.obtener_edad()} años")
print(f"Kilos comidos: {huron1.obtener_kilos_comidos()}")
huron1.comer(0.3)
print(f"Kilos comidos despues de haber comido: {huron1.obtener_kilos_comidos()} kg")
print(f"Cálculo del flete para el Huron: {huron1.calcular_flete()}")

print("-" * 60)

print(f"Nombre de la Boa Constrictor: {boaC1.obtener_nombre()}")
print(boaC1.hacer_sonido())
print(f"Peso: {boaC1.obtener_peso()} kg")
print(f"Edad: {boaC1.obtener_edad()} años")
print(f"Kilos comidos : {boaC1.obtener_kilos_comidos()}")
boaC1.comer(1.0)
print(f"Kilos comidos despues de haber comido: {boaC1.obtener_kilos_comidos()} kg")
print(f"Cálculo del flete para la Boa Constrictor: {boaC1.calcular_flete()}")
print(f"Ratones comidos por la Boa Constrictor: {boaC1.ratones_comidos}")
boaC1.comer_raton()
print(f"Ratones comidos por la Boa Constrictor después de comer ratones: {boaC1.ratones_comidos}")