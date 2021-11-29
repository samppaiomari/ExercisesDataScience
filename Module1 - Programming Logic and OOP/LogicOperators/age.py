#Faire un programme qui demande l'âge de la personne et imprime si elle a plus ou moins de 18 ans.

age = int(input('Insert your age:'))
print('You are under 18 years old.')if age < 18 else print('You are 18 years old or older.')