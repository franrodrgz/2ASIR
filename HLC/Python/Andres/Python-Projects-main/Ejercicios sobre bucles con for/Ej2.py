def main(args):
    a=int(input())
    sum=0
    for a in range(a, a+10):
        sum += a
        print(a)
    print(sum)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))