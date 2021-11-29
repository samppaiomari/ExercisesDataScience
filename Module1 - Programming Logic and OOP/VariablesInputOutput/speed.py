#Demandez à l'utilisateur de rentrer une vitesse initiale (en m/s), une position initiale (en m) et un instant (en s) et affichez la position d'un projectile à cet instant.
#Utilisez la formule mathématique :
#y(t) = y(0) + v(0)*t + (g*(t**2)/2)
#Où, g est l'accélération de la gravité (-10m/s²), y(t) est la position finale, y(0) est la position initiale, v(0) est la vitesse initiale et t est l'instant du temps.

speed = float(input('Insert the initial projectile velocity (m/s): '))
position = float(input('Insert the initial projectile position (m): '))
instant = float(input('Insert the required instant (s): '))
gravity = -10

finalPosition = position + (speed * instant) + (gravity * (instant**2))/2

print(f'The projectile final position at {instant} seconds is {finalPosition} m.')