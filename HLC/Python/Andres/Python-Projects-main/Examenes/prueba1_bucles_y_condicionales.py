import random
def main(args):
	numero_secreto=random.randint(1,100)
	print("Bienvenido al juego de adivinanza de numeros!")
	print("Estoy pensando en un numero del 1 al 100")
	guess=0
	c=0
	while guess != numero_secreto:
		guess=int(input("Introduce tu numero: "))
		if guess > numero_secreto:
			print ("El numero secreto es menor")
		elif guess < numero_secreto:
			print ("El numero secreto es mayor")
		elif numero_secreto == guess:
			c += 1
			print("Felicidades!!! Has adivinado el numero en ",c," intentos")
		c += 1
	return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
