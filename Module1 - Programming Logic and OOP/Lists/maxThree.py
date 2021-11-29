#En utilisant la méthode max(), créez un programme qui imprime les trois plus grands nombres d'une liste.
#Conseil : Utilisez la méthode appropriée pour les listes .remove().

listNumbers = input("Create a list by entering real numbers separated by a comma: \n").split(',')
listNumbers = [float(i) for i in listNumbers ]

print("The three biggest numbers in the list are: \n")
for i in range(3):
    maxN = max(listNumbers)
    print(maxN)
    listNumbers.remove(maxN)
