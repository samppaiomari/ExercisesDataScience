#Faites un programme qui, étant donné deux listes de même taille, imprime le produit scalaire entre celles-ci.
#REMARQUE : le produit scalaire est la somme du résultat de la multiplication entre le nombre en position i de la liste1 par le nombre en position i de la liste2, avec i variant de 0 à la taille de la liste.

listNumbersOne = input("Create the first list by entering real numbers separated by a comma: \n").split(',')
listNumbersOne = [float(i) for i in listNumbersOne]

listNumbersTwo = input("Create the second list with the same size of the first list. Entering real numbers separated by a comma: \n").split(',')
listNumbersTwo = [float(i) for i in listNumbersTwo]

scalarProduct = 0

for i in range(len(listNumbersOne)):
    scalarProduct += (listNumbersOne[i]*listNumbersTwo[i])

print(f'The scalar product is: {scalarProduct}')