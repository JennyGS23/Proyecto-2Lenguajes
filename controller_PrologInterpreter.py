from pyswip import Prolog

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

# Query the Prolog knowledge base
print("\nPrimer consulta: ")
for solucion in prolog_instance.prolog.query('combinaciones_diferentes_cliente(natural, blanca, carbohidratos, sin_postre,  desayuno, 200).'):
    print(solucion)

print("\nsegunda consulta: ")
for solucion in prolog_instance.prolog.query('combinaciones_diferentes_cliente(caliente, roja, vegetales, con_postre,  cena, 500).'):
    print(solucion)

print("\nTercera consulta: ")
for solucion in prolog_instance.prolog.query('combinaciones_diferentes_cliente(natural, roja, vegetales, sin_lacteo, almuerzo, 200).'):
    print(solucion)

