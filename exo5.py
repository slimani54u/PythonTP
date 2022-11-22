

print("Entrez un nombre entier:")
a=int(input())
if a==0 :
    print("Le nombre est zéro (et il est pair)")
elif a > 0 and a%2 == 0 :
    print("Le nombre est positif et pair")
elif a < 0 and a%2 == 0 :
    print("Le nombre est négatif et pair")
elif a < 0 and a%2 == 1 :
    print("Le nombre est négatif et impair")
elif a > 0 and a % 2 == 1:
    print("Le nombre est positif et impair")

