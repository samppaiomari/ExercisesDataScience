#Faire un programme qui demande à l'utilisateur de taper 5 nombres et, à la fin, imprime une liste avec les 5 nombres tapés par l'utilisateur (sans convertir les nombres en int ou float).
#Exemple : Si l'utilisateur tape 1, 5, 2, 3, 6, le programme doit imprimer la liste ['1', '5', '2', '3', '6'].
#Prenez la liste générée et transformez chacun des éléments de cette liste en un float.


listNumbers = []

for i in range(5):
    listNumbers.append(input(f"Enter a number ({i}° position):"))

listNumbers = [float(i) for i in listNumbers]

print(f"Your list with 5 numbers (float): {listNumbers}")