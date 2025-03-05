import os

def manip():
    with open("registro.log", "w") as file:
        file.write("Inicio del registro de operaciones\n")
    os.rename("registro.log", "log_de_sistema.log")
    os.remove("log_de_sistema.log")

def main(args):
    manip()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))