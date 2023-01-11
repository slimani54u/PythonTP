L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
occurence=0
occurenceMax=0
j=0
a=""
for i in range(len(L1)) :
    occurence=0
    for j in range(len(L1)) :
        if L1[i] == L1[j] :
            occurence=occurence+1
            if occurence > occurenceMax :
                occurenceMax =occurence
                a=L1[i]

print(f"Le nombre le plus frequent dans la liste est le : {a} ({occurenceMax} x)")





""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * / """
