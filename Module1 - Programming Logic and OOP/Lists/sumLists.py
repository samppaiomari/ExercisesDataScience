#Faire un programme qui, donné deux listes de même taille, crée une nouvelle liste dont chaque élément est égal à la somme des éléments de la liste 1 et de ceux de la liste 2, à la même position.
#Exemple : étant donné que liste1 = [1, 4, 5] et liste2 = [2, 2, 3], alors liste3 = [1+2, 4+2, 5+3] = [3, 6, 8].

listNumbersOne = input("Create the first list by entering real numbers separated by a comma: \n").split(',')
listNumbersOne = [float(i) for i in listNumbersOne]

listNumbersTwo = input("Create the second list with the same size of the first list. Entering real numbers separated by a comma: \n").split(',')
listNumbersTwo = [float(i) for i in listNumbersTwo]

newList = []

for i in range(len(listNumbersOne)):
    newList.append(listNumbersOne[i]+listNumbersTwo[i])

print(f'The new list is: {newList}')