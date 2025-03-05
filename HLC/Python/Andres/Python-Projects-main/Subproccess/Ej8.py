import subprocess

def ejecuta():
    result = subprocess.run(["bash", "hello.sh"], capture_output=True, text=True)
    print("Salida:", result.stdout)
def main(args):
    ejecuta()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))