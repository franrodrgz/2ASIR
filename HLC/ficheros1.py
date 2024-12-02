#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    try:
        archivo=open("txt.txt")
    except FileNotFoundError:
        print("armendritas")
    for linea in archivo:
        print(linea.strip)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
