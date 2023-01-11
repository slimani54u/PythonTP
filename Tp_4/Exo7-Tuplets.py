# 1)
binome=('slimani',1,'koc',2)
print(f"L'etudiant {binome[2]} est en binome avec l'etudiant {binome[0]}")
# 2)
try:
    binome[2]=input("nouveau binome")
    print(f"L'etudiant {binome[2]} est en binome avec l'etudiant {binome[0]}")
except Exception as e:
    print(e)
    #ce qui signife que les tuples n'accepte pas l'assignement
#3)
try:
    del(binome[2])

except Exception as e:
    print(e)
    #tuple ne supporte pas les suppression d'items

#4)
#les tuples ne peuvent ni ajouter ni enlever de valeur et n'accepte pas l'assignation car ils ont pas de methodes pour
#le domaine d'utilisation des tuplets est restreint et permet d'avoir des valeurs qui ne bougent pas
print(binome)