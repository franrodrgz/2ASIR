import subprocess

def redirect():
    a = subprocess.run(["ls"],capture_output=True,text=True)
    f = open("test.txt","w")
    f.write(a.stdout)
    f.close()
def main(args):
    redirect()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))