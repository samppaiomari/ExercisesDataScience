#Demandez à l'utilisateur de saisir un nombre et imprimez la factorielle de ce numeró.

number = int(input('Please, enter a number: '))
i=1
factorial = 1

while i <= number:
    factorial = factorial * i
    #print(factorial)
    i =i + 1
print(f' The factorial of {number} is {factorial}!')