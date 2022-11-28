


print("Vous cherchez la table de multiplication de quel nombre ?")
a=float(input())
malist=[]
for i in range (10) :
    malist.append(round(a*i,1))
    print(f"{a} * {i} = {malist[i]}")

