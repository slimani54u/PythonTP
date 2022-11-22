import time
# avec la boucle for
n=-1
while n<0 :
    print("saissiez un nombre positif")
    n=int(input())

for i in range (n,-1,-1) :
    print(f"{i}")
    time.sleep(0.2)

# avec la boucle while
import time

n=-1
while n<0 :
    print("saissiez un nombre positif")
    n=int(input())
i=0
while n!=0 :
    n=n-i
    i=1
    print(f"{n}")
    time.sleep(0.2)
