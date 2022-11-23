import random
a=random.randint(0,100)
print("saissisez un nombre entre 0 et 100")
nb=int(input())
i=1
while nb!=a :
    if nb>=0 and nb<=100 :
        if nb>a :
            print("plus petit")
            nb = int(input())
        elif nb<a :
            print("plus grand")
            nb = int(input())
        else :
            break
        i=i+1
    else :
        print("vous n'avez pas saisi un nombre entre 0 et 100")
        nb=int(input())


print(f"vous avez reussi en {i} essai")