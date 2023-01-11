nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
notes = []
somme=0

arret=True
for i in range(nombreEtudiants):
    arret = True
    print("tapez une note")
    a = int(input())
    while arret :

        if a >= 0 and a <= 20:

            somme = a + somme
            notes.append(a)
            arret=False

        else:
            print("mettez une note correcte")
            a = int(input())

moyenne=somme/nombreEtudiants
for i in range(nombreEtudiants):
    print(f"Note etudiant {i} : {notes[i]}")

print(f"moyenne de class {moyenne} \n")

for j in range(nombreEtudiants):
    print(f"{j} | {notes[j]} | {notes[j]-moyenne}")