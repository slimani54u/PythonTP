import os
from datetime import datetime
from genericpath import getsize
a="a.txt"
b="b.txt"
if os.path.isfile(a) and os.path.isfile(b):
    print("1 er fichier : ", getsize(a),"bytes" , "2 eme fichier :",getsize(b),"bytes")
    if  datetime.fromtimestamp(os.path.getmtime(a))< datetime.fromtimestamp(os.path.getmtime(b)):
        print(f"le fichie {a} est plus récent que {b}")
    else: print(f"le fichie {b} est plus récent que {a}")