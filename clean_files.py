
 # 
 #     repo:   https://github.com/mda-solutions
 #     author: moises.rangel@gmail.com
 #
 # Licensed under the MIT License (the "License"); you may
 # not use this file except in compliance with the License. You may obtain
 # a copy of the License at
 #
 #     http://opensource.org/licenses/MIT
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.
 #

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

