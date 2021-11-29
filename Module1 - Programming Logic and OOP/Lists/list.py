#Créez une liste au choix et réalisez un programme qui imprime chaque élément de la liste en utilisant for.

listM = ['Mariana', True, 1, 2.3, "22 years old"]
print("Printing list: \n")
#First Method:
for i in listM:
    print(i)

print("\nPrinting list: \n")
#Second Method:
for i in range(len(listM)):
    print(listM[i])