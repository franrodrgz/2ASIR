import sys
import re
def lectura(texto):
    f=open(texto,'r')
    a=f.read()
    f.close()
    return a
def check(x):
    patron = r'\b\d{1,3}[.]\d{1,3}[.]\d{1,3}.\d{1,3}'
    test = re.search(patron, x)
    print(test.group())

def main(args):
    patron = sys.argv[1]
    patron =lectura(patron)
    check(patron)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))