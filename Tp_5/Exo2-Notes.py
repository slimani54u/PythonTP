b=0
moyenne=0
for i in range(0,5):
    a = input("Veuillez entrer la note du module 1 et le coefficient correspondant :")
    tab=a.split(" ")
    moyenne=float(tab[0])*float(tab[1])+moyenne
    if int(tab[0])<8:
        b=b+1
moyenne=moyenne/5
print("la moyenne général correspond à :",moyenne)
if moyenne>10 and b==0:
    print("L’étudiant est admis ")
else:
    print("L’étudiant n'est pas admis ")


