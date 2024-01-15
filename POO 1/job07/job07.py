class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation de la classe Personnage
personnage_instance = Personnage(2, 3)

# Affichage de la position initiale
print("Position initiale:", personnage_instance.position())

# Déplacement vers la gauche
personnage_instance.gauche()
print("Position après déplacement gauche:", personnage_instance.position())

# Déplacement vers la droite
personnage_instance.droite()
print("Position après déplacement droite:", personnage_instance.position())

# Déplacement vers le haut
personnage_instance.haut()
print("Position après déplacement haut:", personnage_instance.position())

# Déplacement vers le bas
personnage_instance.bas()
print("Position après déplacement bas:", personnage_instance.position())
