import sys
def main():
    print("Introduce tu nota")
    a=int(input())
    if a>=9:
        print("SB")
    elif a>=8:
        print("NT")
    elif a>=6:
        print("BI")
    elif a>=5:
        print("SF")
    else:
        print("IN")
    return 0
if __name__ == '__main__':
    sys.exit(main())