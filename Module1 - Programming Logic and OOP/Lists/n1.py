#Faire un programme qui demande à l'utilisateur de taper un nombre n et imprimer une liste avec tous les nombres de 0 à n-1.
#Exemple : si l'utilisateur tape 5, le programme doit imprimer [0, 1, 2, 3, 4].

number = int(input("Please enter an integer number:"))
print(f"Your number is {number}.\n")
for i in range(number):
    print(i)
