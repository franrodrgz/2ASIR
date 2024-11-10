# Diseña una función en python que reciba como parámetro una cadena de texto y devuelva True si es
# un correo electrónico y False si no lo es. No es necesario que diseñes el patrón, puedes encontrarlo
# facilmente en internet

import re

def correo_electronico(cadena):
    # Patrón para validar direcciones de correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Utilizamos la función match() del módulo re para verificar si la cadena coincide con el patrón
    if re.match(patron, cadena):
        return True
    else:
        return False

# Funcionamiento de la funcion
email = input("Introduce un email para comprobar si es valido o no: ")
resultado = correo_electronico(email)

if resultado:
    print(f"{email} es un correo electrónico válido.")
else:
    print(f"{email} no es un correo electrónico válido.")

            