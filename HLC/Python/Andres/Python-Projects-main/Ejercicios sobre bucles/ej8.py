
def main(args):
    a=int(input(""))
    b=1
    factorial = 1
    if a > 0:
        while b<=a:
          factorial *= b
          b +=1
    print(factorial)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
