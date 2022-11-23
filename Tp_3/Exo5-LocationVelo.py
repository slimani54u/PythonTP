print("Donnez l’heure de début de la location (un entier)")
a=int(input())
print("Donnez l’heure de fin de la location (un entier)")
b=int(input())

Ttotal=0
10
while True :
    if b >a and b in range(0, 25) or b-a<=24 and b >a and b in range(0, 25):

        if  a in range(0, 8) and b in range(0, 8) :
            Ttotal=b-a
            print("Vous avez loué votre vélo pendant")
            print(f"{Ttotal}heure(s) au tarif horaire de 1.0 euro(s)")
            print(f"Le montant total à payer est de {Ttotal}euro(s).")
            break

        if a in range(17, 25) and b in range(17, 25) :
            Ttotal = b - a
            print("Vous avez loué votre vélo pendant")
            print(f"{Ttotal} heure(s) au tarif horaire de 1.0 euro(s)")
            print(f"Le montant total à payer est de {Ttotal}euro(s).")
            break
        if a in range(7, 18) and  b in range(7, 18):
            Ttotal = (b - a)*2
            print("Vous avez loué votre vélo pendant")
            print(f"{Ttotal} heure(s) au tarif horaire de 1.0 euro(s)")
            print(f"Le montant total à payer est de {Ttotal}euro(s).")
            break
        if a in range(0, 8) and  b in range(7, 18):
            c = b - 17
            a = 7 - a
            Ttotal =a+c*2
            print("Vous avez loué votre vélo pendant")
            print(f"{a} heure(s) au tarif horaire de 1.0 euro(s)")
            print(f"{c} heure(s) au tarif horaire de 2.0 euro(s)")
            print(f"Le montant total à payer est de {Ttotal}euro(s).")
            break
        if a in range(0, 8) and b in range(17, 25):
            c=b-17
            a=7-a
            d=(b-c-a)
            Ttotal = c +(b-c-a)*2 +a
            print("Vous avez loué votre vélo pendant")
            print(f"{a+c} heure(s) au tarif horaire de 1.0 euro(s)")
            print(f"{d} heure(s) au tarif horaire de 2.0 euro(s)")
            print(f"Le montant total à payer est de {Ttotal} euro(s).")
            break

        if a in range(7, 18) and b in range(17, 25):
            a=17-a
            b=b-17
            Ttotal =a*2+b
            print("Vous avez loué votre vélo pendant")
            print(f"{b}heure(s) au tarif horaire de 1.0 euro(s)")
            print(f"{a}heure(s) au tarif horaire de 2.0 euro(s)")
            print(f"Le montant total à payer est de {Ttotal}euro(s).")
            break
    else :
        if not a in range(0, 24) :

            a = int(input("l'heure de début doit etre entre 0 et 23 :"))
        if not b in range(0, 25):
            b = int(input("entrer l'heure de fin doit etre entre 0 et 24 :"))
        if b-a==0 :
            print("attention l'heure de debut est identique a l'heure de fin")
            a = int(input("ressayer entrer l'heure de début :"))
            b = int(input("ressayer entrer l'heure de fin :"))
        if b<a :
            print("Attention ! le début de la location est après la fin")
            a = int(input("ressayer entrer l'heure de début :"))
            b = int(input("ressayer entrer l'heure de fin ;"))
