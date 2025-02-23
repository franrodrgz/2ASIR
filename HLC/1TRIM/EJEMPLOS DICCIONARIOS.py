#  EJEMPLOS DICCIONARIOS  
#  Los diccionarios son objetos iterables, mutables y desordenados.
#  Cada elemento se compone de una clave (que debe ser un objeto inmutable) y un valor para la clave
#  El valor puede ser cualquier tipo de objeto (números, cadenas, tuplas, listas, diccionarios...)

def main(args):
	# Hay muchas formas de crear un diccionario

	# Podemos crear un diccionario vacío
	miDiccionarioVacio={}

	# O podemos crear un diccionario dándole valores

	a = dict(A=1, Z=-1)
	b = {'A': 1, 'Z': -1}
	c = dict(zip(['A', 'Z'], [1, -1]))
	d = dict([('A', 1), ('Z', -1)])
	e = dict({'Z': -1, 'A': 1})
	print(a == b == c == d == e)  # are they all the same?
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)

	# Los valores pueden ser muchas cosas
	# Esto es un diccionario cuyos valores son tuplas
	notas={'Mates':(5,6.5,9),'Lengua':(7,6),'Inglés':(5,9.5,8,4)}
	print("\nDiccionario cuyos valores son tuplas")
	print(notas)

	# Esto es un diccionario cuyos valores son listas
	notas={'Mates':[5,6.5,9],'Lengua':[7,6],'Inglés':[5,9.5,8,4]}
	print("\nDiccionario cuyos valores son listas")
	print(notas)

	# Recuerda que son objetos iterables pero observa el resultado de el siguiente código
	print("\n")
	for asignatura in notas:
		print(asignatura)

	# ¡OJO! Al no ser elementos ordenados no podemos usar indexación

    # Podemos saber cuantas claves hay metidas
	print(f"\nHay {len(notas)} asignaturas en el diccionario")

	# Podemos acceder a los valores usando las claves
	print(f"\nLas notas de Mates son: {notas['Mates']}")

	# Podemos averiguar si una clave está en el diccionario
	if('Lengua' in notas): print("\nTenemos las notas de Lengua registradas")

	# Podemos borrar los valores asociados a una clave concreta
	print("\nVamos a borrar las notas de Inglés")
	del notas['Inglés']
	print("Mira, ya están borradas")
	print(notas)
	print("\nVamos a añadir las de Latín")
	notas["Latín"]=(2.5,4,5.5)
	print(notas)

	# Puedo usar todas las claves, por ejemplo para mostrarlas
	print(f"\nEsto son todas las claves :{notas.keys()}")

	# Puedo usar todas los valores, por ejemplo para mostrarlos
	print(f"\nEsto son todos los valores :{notas.values()}")

	# Puedo usar todos los elementos, por elemeplo para mostrarlos
	print(f"\nEsto son todos los elementos :\n{notas.items()}")

	# También puedo iterar por ellos
	print("\nTodas las claves de una en una")
	for clave in notas.keys():
		print(clave)

	print("\nTodos los valores de uno en uno")
	for valor in notas.values():
		print(valor)
	# Recuerda, en este ejemplo los valores son tuplas. Es un buen ejercicio
	# tratar de mostrar los elementos de esas tuplas uno a uno. Inténtalo.
	
	print("\nTodos los elementos de uno en uno")
	for elemento in notas.items():
		print(elemento)
	print("\nYa no necesito el diccionario. Lo voy a borrar")
	notas.clear()
	print("Observa, ya no hay nada")
	print(notas)
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))