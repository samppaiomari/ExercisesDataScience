#Calculez la somme des mille termes des inverses des factorielles : 1/(1 !) + 1/(2 !) + 1/(3 !) + 1/(4 !) + ...
#Conseil 1 : Utilisez trois variables : un compteur, une variable pour la somme et une variable pour les termes. 
#Conseil 2 : Rappelez-vous que 4 ! = 4*3*2*1 qui est aussi égal à 4*3!

limit = int(input("This program sums up to a thousand terms of the series 1/n! Enter up to which term you want to sum: "))
j = 1
sumS = 0
factorial = 1

while j <= limit:
    sumS += 1/factorial
    j += 1
    factorial = factorial * j
    
print(f' The total sum of the terms is {sumS}!')