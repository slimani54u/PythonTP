# boucle for
print("quelle boucle voulez vous choisir for ou while ")
a=input()
if a=='for' :
    print("choisissez un nombre")
    n = int(input())
    d = n
    s = 1
    if n != 0:
        for i in range(1, n + 1, 1):
            s = i * s
            print(s)
        print(f"la factorielle du nombre {d} est {s}")
    else:
        print(f"la factorielle du nombre 0 est 1")

elif a=='while':
#boucle while
    print("choisissez un nombre")
    n = int(input())
    n=n+1
    i=1
    d=n
    s=1
    if n!=0 :
        while i!=n :
            s = i * s
            i=i+1
            print(s)
        print(f"la factorielle du nombre {d} est {s}")

    else:print(f"la factorielle du nombre 0 est 1")