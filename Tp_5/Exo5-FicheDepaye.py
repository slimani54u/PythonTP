Sh=int(input("quelle est votre salaire horraire"))
horaire=int(input("quelle est le nombre d'heure de travail"))

if horaire<160:
    print(Sh*horaire)
elif horaire>160 and horaire<=200:
    print(Sh*1.25 * (160-horaire)+Sh*160)
else:
    y=200-horaire
    print(Sh*1.5 * y + Sh*1.25*(160-y)+Sh*160)
