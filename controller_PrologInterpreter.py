from typing import Self
from pyswip import Prolog
from controller_Main import DatabaseConnection
import model_MealHealthyDAO
from model_MealHealthy import HealthyMeal
import re

connection_string = DatabaseConnection()
# Singleton design pattern
class PrologInterpreter:
    # Private class variable to hold the singleton instance
    _instance = None

    # Override the default __new__ method to ensure only one instance is created
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PrologInterpreter, cls).__new__(cls)
            cls._instance.prolog = Prolog()
            cls._instance.prolog.consult('filtros.pl')
        return cls._instance

# Create an instance of the PrologInterpreter
prolog_instance = PrologInterpreter()
database = model_MealHealthyDAO.HealthyMealDAO(connection_string)



def obtener_combinaciones_prolog(Bebida, Proteina, Acompanamiento, Postre, MomentoDelDia, CaloriasMinimas):
    prolog = Prolog()
    prolog.consult('filtros.pl')

    prolog.query('consulta_combinaciones({Bebida},  {Proteina}, {Acompanamiento}, {Postre}, {MomentoDelDia}, {CaloriasMinimas}).')



Bebida = 'natural'
Proteina = 'blanca'
Acompanamiento = 'carbohidratos'
Postre = 'sin_postre'
MomentoDelDia = 'desayuno'
CaloriasMinimas = 200

combinaciones = obtener_combinaciones_prolog(Bebida, Proteina, Acompanamiento, Postre, MomentoDelDia, CaloriasMinimas)


# Abre el archivo y lee las líneas
with open('respuesta.txt', 'r') as file:
    lines = file.readlines()

# Patrón de búsqueda utilizando expresiones regulares
pattern = r'{Bebida:(.*?),Proteina:(.*?),Acompanamientos:\[(.*?)\],Postre:(.*?),Calorias:(\d+)}'

# Itera a través de las líneas y extrae los componentes
for line in lines:
    match = re.search(pattern, line)
    if match:
        bebida = match.group(1)
        proteina = match.group(2)
        acompanamientos = match.group(3).split(',').pop()
        postre = match.group(4)
        calorias = int(match.group(5))

        database.setMeal(bebida, proteina, acompanamientos, postre, calorias)





