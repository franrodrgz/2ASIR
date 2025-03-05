def main(args):
	tupla=("@gmail.com","192.168.100.50")
	lista=list()
	x=tupla[1].split(".")
	y=int(x[3])
	print(y)
	for i in range(0,20):
		c=y
		tupla2=("usuario"+str(i)+tupla[0],"192.168.100."+str(c))
		lista.append(tupla2)
		y+=1

	print(lista)
	for usuario, ip in lista:
		print("Usuario: ",usuario," Ip: ",ip)
	return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))