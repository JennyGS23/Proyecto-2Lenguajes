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
    query = f'combinaciones_diferentes_cliente({Bebida}, {Proteina}, {Acompanamiento}, {Postre}, {MomentoDelDia}, {CaloriasMinimas}).'
    
    for solucion in prolog_instance.prolog.query(query):
        None



if __name__ == '__main__':
    Bebida = 'caliente'
    Proteina = 'marino'
    Acompanamiento = 'calientes'
    Postre = 'sin_postre'
    MomentoDelDia = 'cena'
    CaloriasMinimas = 600

    combinaciones = obtener_combinaciones_prolog(Bebida, Proteina, Acompanamiento, Postre, MomentoDelDia, CaloriasMinimas)


# # Abre el archivo y lee las líneas
# with open('combinaciones.txt', 'r') as file:
#     lines = file.readlines()

