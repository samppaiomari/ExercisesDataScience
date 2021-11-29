#Réalisez un programme qui lit la vitesse d'une voiture, et dit si elle dépasse la vitesse autorisée de 50 km/h ou non. Si la voiture dépasse la vitesse autorisée, le programme doit imprimer que le conducteur a excédé la vitesse autorisée et a reçu une amende d'un certain montant. 
#Pour calculer la valeur de l'amende, on considère que par kilomètre de vitesse supérieure à la limite autorisée, le conducteur doit payer 10 reais.

speedLimit = float(input('Insert the speed of the car:'))

if speedLimit>50:
    print('Such an irresponsability! You are above the allowed velocity!')
    print(f'You will have to pay a fine of R$ { int(speedLimit - 50)*10} .')
else:
    print('Great! You are within the allowed speed range!')