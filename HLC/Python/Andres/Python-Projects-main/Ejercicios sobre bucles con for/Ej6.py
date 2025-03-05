def main(args):
    a=int(input())
    b=int(input())
    s=0
    for a in range(a, b+1):
        s += a
    s=s/a
    print(s)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))