#Réalisez un programme qui demande à l'utilisateur de saisir l'âge, le salaire et le sexe d'une personne jusqu'à ce que les entrées saisies soient valides.
#Âge : de 0 à 150 ans ;
#Salaire : supérieur à 0 ;
#Sexe : M, F ou autre.

name = input("Hello! Enter the person's name:")

age = int(input(f"Now, enter {name}'s age in numbers of years:"))
while age<=0 or age>=150:
    age = int(input("Are you sure he/she is alive haha?? Invalid input! Insert an age again: "))

wage = round(float(input(f"Now, enter {name}'s wage using numbers (dollars):")),2)
while wage<=0:
    wage = round(float(input(f"Oops! Invalid input, enter {name}'s wage again:")),2)

sex = input(f"Finally, tape {name}'s sex (Woman/Man/Other):").strip()[0].upper()
while sex != 'W' and sex!='M' and sex != 'O':
    sex = input("It was not possible to understand you! Invalid input! Insert again: ").strip()[0].upper()
    
