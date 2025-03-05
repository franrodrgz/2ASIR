#!/usr/bin/env python3

import sys


def main(args):

	print("Indica el número inicial: ")
	i=int(input())
	sum=0
	
	for i in range (i,i+10):
		sum += i
		print(i)
	print("La suma da un total de: ",sum)
	media=sum/i
	print("La media es: ",media)
	return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
