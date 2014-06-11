import os

def cutit(s,n):    
   return s[n:]

def clean(phpfile):
    tosearch = "$gpnarcbpgy"
    f = open(phpfile)
    if tosearch in f.read():
        print "Limpiando $gpnarcbpgy en: " + phpfile
        f = open(phpfile,"r")
        lines = f.readlines()
        f.close()
        f = open(phpfile,"w")

        for line in lines:
            if line.startswith("<?php $gpnarcbpgy"):
                lastindex = line.index("$iysbebbcuf-1; ?>") + 17
                newline = cutit(line, lastindex)
                f.write(newline)
            else:    
                f.write(line)

        f.close()


def main():
    path = "/path/to/site/root"
    phpfiles = [os.path.join(root, name) for root, dirs, files in os.walk(path) for name in files if name.endswith((".php"))]
    
    for phpfile in phpfiles:
        clean(phpfile)
        

if __name__ == '__main__':
    main()

