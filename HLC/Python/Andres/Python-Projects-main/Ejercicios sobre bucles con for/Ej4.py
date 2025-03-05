def main(args):
    a=int(input())
    b=int(input())
    sum=0
    for a in range(a,b+1):
        sum += a
    print(sum)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))