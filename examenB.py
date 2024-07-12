import random
import math
import csv
import statistics
nombre_archivo = 'planilla_de_sueldos.csv()'

trabajadores = ["Juan Perez", "Maria Garcea", "Carlos Lopez", "Ana Martinez", 
                "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", 
                "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

def generar_sueldos_aleatorios():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos

sueldos = generar_sueldos_aleatorios()
print(sueldos)

