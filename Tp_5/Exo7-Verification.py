import os
from datetime import datetime
from genericpath import getsize
a=input("1 er fichier")
b=input("2 eme fichier")
if os.path.isfile(a) and os.path.isfile(b):
    print("1 er fichier"+getsize(a), "2 eme fichier"+getsize(b))
    if  datetime.datetime.fromtimestamp(os.path.getmtime(a))<datetime.datetime.fromtimestamp(os.path.getmtime(b)):
        print(f"le fichie {a} est plus récent que{b}")
    else: print(f"le fichie {b} est plus récent que{a}")