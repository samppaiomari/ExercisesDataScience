#Créez un programme qui vous demande votre salaire horaire et le nombre d'heures travaillées dans le mois, puis calculez et affichez votre salaire total pour ce mois.

hourlywage = float(input('Insert your hourly wage: '))
monthlyhours = float(input('Insert the number of your monthly hours worked: '))
print(f'Your monthly salary is {hourlywage * monthlyhours} dollars')