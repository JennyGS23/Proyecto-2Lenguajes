from pyswip import Prolog



# # Crear una instancia global de Prolog
# prolog_instance = Prolog()

# # Definir reglas y hechos en la instancia de Prolog
# prolog_instance.assertz("hombre(juan)")
# prolog_instance.assertz("mujer(maria)")

# # Consultar hechos y reglas
# list_of_men = list(prolog_instance.query("hombre(X)"))
# list_of_women = list(prolog_instance.query("mujer(X)"))

# # Imprimir los resultados
# print("Hombres:")
# for result in list_of_men:
#     print(result["X"])

# print("\nMujeres:")
# for result in list_of_women:
#     print(result["X"])



# Crea una instancia de Prolog
prolog = Prolog()

# Carga el archivo de Prolog
prolog.consult('filtros.pl')

# Ahora puedes hacer consultas en Prolog desde Python
for solucion in prolog.query('combinaciones_diferentes_cliente(caliente, marino, calientes, sin_postre,  cena, 600).'):
    print(solucion)
