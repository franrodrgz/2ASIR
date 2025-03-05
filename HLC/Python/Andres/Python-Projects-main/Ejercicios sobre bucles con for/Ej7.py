def main(args):
    a=int(input())
    mul=0
    for i in range(1,11):
        mul=a*i
        print(a," x ",i," = ",mul)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))