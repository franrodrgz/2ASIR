import os
import shutil

def comprimir():
    os.mkdir("proyecto")
    os.mkdir("proyecto/datos")
    os.mkdir("proyecto/scripts")
    os.mkdir("proyecto/informes")
    shutil.make_archive("proyecto", "zip", "proyecto")
    shutil.unpack_archive("proyecto.zip", "proyecto_descomprimido")

def main(args):
    comprimir()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))