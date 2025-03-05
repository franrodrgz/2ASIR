import os
import shutil
import subprocess

def dircopy():
    shutil.copytree("proyecto", "proyecto_backup")
    with open("backup.log", "w") as log:
        log.write("Backup realizado con éxito\n")
    subprocess.run(["ls", "-l", "proyecto_backup"], text=True)
    
def main(args):
    dircopy()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))