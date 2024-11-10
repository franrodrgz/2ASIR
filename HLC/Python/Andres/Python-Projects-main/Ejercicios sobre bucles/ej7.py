def main(args):
    a=int(input())
    b=int(input())
    c=int(input())
    mul=0
    while a<=b:
        mul=a*c
        print(a," x ",c," = ",mul)
        a += 1
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
