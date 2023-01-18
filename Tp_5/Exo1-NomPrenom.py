p1=input("Inscrivez votre Prenom :")
n1=input("Inscrivez votre Nom :")


print()
p2=input("Inscrivez votre Prenom :")
n2=input("Inscrivez votre Nom :")



if n1>n2 :
    print(n2.upper(),p2.capitalize())
elif n2>n1:
    print(n1.upper(), p1.capitalize())
elif p1 >p2:
    print(n2.upper(), p2.capitalize())
elif p2>p1:
    print(n1.upper(), p1.capitalize())
else:
    print("meme prenom meme nom")
