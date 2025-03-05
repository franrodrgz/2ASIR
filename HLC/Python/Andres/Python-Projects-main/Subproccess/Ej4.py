import os
import shutil

def copiaymv():
    os.mkdir("backup")
    os.mkdir("backup_final")
    with open("documento.txt","w") as file:
        file.write("hola")
    shutil.copy("documento.txt", "backup/")
    shutil.move("backup/documento.txt", "backup_final/")

def main(args):
    copiaymv()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))