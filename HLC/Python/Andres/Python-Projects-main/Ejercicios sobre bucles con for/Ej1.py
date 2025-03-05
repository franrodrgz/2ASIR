def main(args):
    a=int(input())
    b=int(input())
    for a in range(a,b+1):
        print(a)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))