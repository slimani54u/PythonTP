L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

occurenceMax=0


for i in range(len(L1)) :
    if occurenceMax<L1.count(L1[i]) :
        occurenceMax=L1.count(L1[i])
        a=L1[i]
print(f"Le nombre le plus frequent dans la liste est le : {a} ({occurenceMax} x)")





""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * / """
