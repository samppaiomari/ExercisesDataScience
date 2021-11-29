#Calculez la somme de jusqu'à mille termes de la série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...
#Conseil 1 : Utilisez trois variables :
    #un compteur, qui commence à zéro ;
    #une variable pour la somme de tous les termes, qui commence également à zéro ;
    #une variable pour chaque terme, qui commence à 1 et à chaque loop est divisée par 2.
#Conseil 2 : La répétition de la somme de mille termes peut être faite avec la fonction while counter < 1000.

limit = int(input("This program sums up to a thousand terms of the series 1/2^n! Enter up to which term you want to sum: "))
i = 0
sumS = 0
term = 1
while i<limit:
    sumS += term 
    term = term/2
    i += 1
print(f' The total sum of the terms is {sumS}!')