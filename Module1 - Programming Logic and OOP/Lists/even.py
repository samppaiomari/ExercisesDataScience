#Créez un programme qui examine tous les éléments d'une liste et indique combien d'entre eux sont des paires.

listNumbers = input("Create a list by entering integer numbers separated by a comma: \n").split(',')
evenNumbers = []
index = 0

for i in listNumbers:
    if int(i)%2 == 0:
        evenNumbers.append(int(i))
    listNumbers[index] = int(i)
    index +=1

print(f"\nYour list: {listNumbers}")
print(f"There is {len(evenNumbers)} even numbers in your list!")
print(f"Even numbers in your list: {evenNumbers}")
