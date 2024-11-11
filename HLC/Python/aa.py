#!/usr/bin/env python3

import sys


def main(args):

	print("Indica el número inicial: ")
	i=int(input())
	print("Indica el número final: ")
	b=int(input())
	sum=0
	c=0
	if i>b:
		c=i
		i=b
		for b in range (b,c+1):
			sum += b
			print(b)
	else:
		for i in range (i,b+1):
			sum += i
			print(i)
	print("La suma da un total de: ",sum)
	media=sum/i
	print("La media es: ",media)
	return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
