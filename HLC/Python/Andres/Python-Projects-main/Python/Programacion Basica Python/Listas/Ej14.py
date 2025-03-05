def createMatrix():
    matriz=[]
    for i in range(0,2):
        fila=[]
        for j in range(0,2):
            valor = int(input(f"Introduce el valor de la matriz[{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumMatrix(matrix1,matrix2):
    matriz=[]
    for i in range(0,2):
        fila=[]
        for j in range(0,2):
            valor = matrix1[i][j] + matrix2[i][j]
            fila.append(valor)
        matriz.append(fila)
    return matriz
def main(args):
    print("Introduce los valores de la matriz 1")
    matrix1=createMatrix()
    print("Introduce los valores de la matriz 2")
    matrix2=createMatrix()
    print(sumMatrix(matrix1,matrix2))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))