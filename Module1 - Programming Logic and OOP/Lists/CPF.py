#Réalisez un programme qui demande à l'utilisateur d'entrer le CPF et de vérifier s'il est valide. 
#Tout d'abord, le programme doit multiplier chacun des 9 premiers chiffres du CPF par les nombres 10 à 2 et faire la somme de toutes les réponses. 
#Le résultat doit être multiplié par 10 et divisé par 11. Le reste de cette division doit être égal au premier chiffre de contrôle ( dixième chiffre). 
#Ensuite, le programme doit multiplier chacun des 10 premiers chiffres du CPF par les nombres 11 à 2 et répéter la procédure précédente pour vérifier le deuxième chiffre de vérification.

#Exemple -> Si le CPF est 286.255.878-87, le programme doit d'abord faire :
#   x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)
#Ensuite, le programme doit tester si 
#   x*10%11 == 8 (le dixième chiffre du CPF)
#Si c'est le cas, le programme doit calculer :
#   x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)
# et vérifier que x*10%11 == 7 (le onzième chiffre du CPF).

#Requesting CPF:
CPF = input("Please enter your CPF (only numbers): ").strip()
CPF = [int(i) for i in CPF]

#First step:
num = 10
sum = 0

for i in range(9):
    sum += num*CPF[i]
    i +=1
    num -=1

#Second Step:
if (sum*10)%11 == CPF[9]:

    #Third Step:
    num = 11
    sum = 0

    for i in range(10):
        sum += num*CPF[i]
        i +=1
        num -=1
    
    #Fourth step:
    if (sum*10)%11 == CPF[10]:
        print(f"Congrats! Your CPF {CPF[0]}{CPF[1]}{CPF[2]}.{CPF[3]}{CPF[4]}{CPF[5]}.{CPF[6]}{CPF[7]}{CPF[8]}-{CPF[-2]}{CPF[-1]} is validated!")
    else:
        print("Ooops, we found a problem!")
else:
    print("Ooops, we found a problem!")

