#Faire un programme qui imprime le plus grand nombre dans une liste, sans utiliser la méthode max().

listNumbers = input("Create a list by entering real numbers separated by a comma: \n").split(',')
maxN = float(listNumbers[0])
for i in listNumbers:
    if float(i) > maxN:
        maxN = float(i)

print(f"The biggest number in your list is {maxN}")
