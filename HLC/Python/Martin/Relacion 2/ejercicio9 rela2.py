def main(args):
    print("Introduce tres números para ordenarlos de mayor a menor")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    if n1 >= n2 and n1 >= n3:
        if n2 >= n3:
            print("Números ordenados de mayor a menor:", n1, n2, n3)
        else:
            print("Números ordenados de mayor a menor:", n1, n3, n2)
    elif n2 >= n1 and n2 >= n3:
        if n1 >= n3:
            print("Números ordenados de mayor a menor:", n2, n1, n3)
        else:
            print("Números ordenados de mayor a menor:", n2, n3, n1)
    else:
        if n1 >= n2:
            print("Números ordenados de mayor a menor:", n3, n1, n2)
        else:
            print("Números ordenados de mayor a menor:", n3, n2, n1)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


