nMax=10
v1=[]
v2=[]
n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))
i=0

while True:

    if n >= 1 and n < nMax:
        print(f"saisissez les {n} du premier vecteur")
        for i in range(n):

            v1.append(int(input()))

        print(f"saisissez les {n} du deuxieme vecteur")
        for i in range(n):

            v2.append(int(input()))


    break
else :
    n = int(input("la taille de vos vecteurs doit être [entre 1 et 10]"))

produit=0
print("saisie du premier vecteur :")
for i in range (n) :
    print(f" v1{[i]} = {v1[i]}")

    produit=v1[i]*v2[i]+produit

print("saisie du deuxieme vecteur :")
for i in range (n) :
    print(f" v2{[i]} = {v2[i]}")

print(f"le produit scalaire de v1 et v2 vaut {produit}")