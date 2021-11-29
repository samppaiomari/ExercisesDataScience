#Créez un programme qui demande à l'utilisateur un nombre et imprime tous les nombres de un jusqu'au nombre donné.

number = int(input('Please, enter a number: '))
i = 1

print(f'Numbers from 1 to {number}:\n')
while i <= number:
    print(i)
    i += 1