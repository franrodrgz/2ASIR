def main(args):
    i = int(input())
    b = int(input())
    while i <= b:
        print(i)
        i += 1
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))