L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
a=0
i=0
b=0
for i in range(0,len(L1)) :

    if L1.count(L1[i]) > a :
        a=L1.count(L1[i])
        b=L1[i]


print(f"Le nombre le plus frequent dans la liste est le : {b} ({a} x)")





""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * / """
