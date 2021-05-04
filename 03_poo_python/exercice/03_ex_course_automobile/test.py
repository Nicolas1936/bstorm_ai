from voiture import Voiture
from circuit import Circuit
from course import Course

spa = Circuit('SPA', 1000)

v1 = Voiture('Peugeot', 200, 250)
v2 = Voiture('Renault', 150, 160)
v3 = Voiture('Ferrari', 210, 250)
v4 = Voiture('Mercedes', 220, 250)

c = Course(spa, 4)


c.ajout_voiture(v1)
c.ajout_voiture(v2)
c.ajout_voiture(v3)
c.ajout_voiture(v4)

c.start()