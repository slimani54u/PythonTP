# a)
n=int(input())
somme=0
for i in range (n):
    somme=i+somme
print(somme)

# b)
n=0
while n !=100 :
    print("vous en attentes entrez la bonne valeur")
    n=int(input())

print("vous avez entrez la bonne valeur")

# c)
n = 100.0
d = 0
a = 0
b = 0
c = 0
arret = True
while arret:
    if n >= 0 and n <= 20:

        while d != 10:
            if n >= 0 and n <= 20:
                if n < 10:
                    a = a + 1
                    d = d + 1
                    print("taper le prochain nombre qui doit etre entre 0 et 20")
                    n = float(input())

                elif n >= 10 and n < 15:
                    b = b + 1
                    d = d + 1
                    print("taper le prochain nombre qui doit etre entre 0 et 20")
                    n = float(input())

                elif n >= 15:
                    c = c + 1
                    d = d + 1
                    print("taper le prochain nombre qui doit etre entre 0 et 20")
                    n = float(input())

            else:
                print("taper un nombre qui doit etre entre 0 et 20")
                n = float(input())
        if d == 10:
            arret = False
    else:
        print("taper un nombre qui doit etre entre 0 et 20")
        n = float(input())

print(f"Le nombre de valeurs inférieur strictement à 10 est de {a}")
print(f"Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est de {b}")
print(f"Le nombre de valeurs supérieur ou égale à 15 est de {c}")

# d)
n = 0
while n < 1:
    print("saisissez une valeur supérieur à 1")
    n = int(input())
s = n
i = 0
while s > 0:
    s = s - i
    i = i + 1

i=i-1
print(f"le plus grand nombre N est {i}")