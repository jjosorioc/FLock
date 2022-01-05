"""
Archivo para probar cosas
"""


import os

# Current directory os.getcwd()

"""
Change current directory => os.chdir("/home/user/Documents")

La estructura de los arhivos depende del sistema operativo

"""

# Current directory
os.chdir("path")


# Lista con todos los folders y arhivos
lista = os.listdir()

print(lista)