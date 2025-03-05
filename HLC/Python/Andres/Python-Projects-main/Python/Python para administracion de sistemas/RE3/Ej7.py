import subprocess

def ping():
    try:
        a = subprocess.run(["ping","-c","5","google.com"],capture_output=True,text=True)
        f = open("test.txt","w")
        f.write(a.stdout)
        f.close()
    except Exception as e:
        print("Error en ping:", e)
def main(args):
    ping()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))