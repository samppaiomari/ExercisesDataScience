#Réalisez un programme, utilisant des loops, qui demande à un utilisateur de saisir un nombre et qui se termine seulement lorsque l'utilisateur tape 0. A la fin, imprimez la somme de tous les nombres tapés.

print("Welcome! Here, you should enter the numbers you want to sum! To stop the program, you must enter '0'!")
number = float(input('Please, enter a number: '))
sumT = 0
while number != 0:
    sumT += number
    number = float(input('Please, enter a number again: '))
    
print(f'Total sum is {sumT}!')