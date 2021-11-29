#Faire un programme qui demande le rayon d'un cercle, calcule et affiche son aire.
#Remarque : Formule de l'aire d'un cercle : A = 3,14*(r**2), avec 'r' le rayon.

radius = float(input("Insert the circle radius:"))
area = (3.14 * (radius ** 2))
print(f'For radius (meters): {radius} ; The area (square meters) is: {area}')