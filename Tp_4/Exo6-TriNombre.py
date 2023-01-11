l=[5, 2, 4, 8, 1, 3]
def sorted(liste):
    print(l)
    for i in range(0,len(l)-1):
        min=l[i]
        indice=i


        for j in range(i+1,len(l)):
            if l[j]<min:
                min=l[j]
                indice=j
        if indice !=i :
            tmp=l[i]
            l[i]=min
            l[indice]=tmp

        print(l)





#sorted(l)



l.sort()
print(l)
#Remarque tri automatiquement la liste