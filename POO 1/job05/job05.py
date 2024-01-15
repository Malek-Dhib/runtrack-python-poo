class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée x est : {self.x}")

    def afficherY(self):
        print(f"La coordonnée y est : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y
        
# Exemple d'utilisation de la classe Point
point_instance = Point(3, 4)

# Affichage des coordonnées initiales
point_instance.afficherLesPoints()

# Affichage de la coordonnée x
point_instance.afficherX()

# Affichage de la coordonnée y
point_instance.afficherY()

# Changement de la valeur de la coordonnée x
point_instance.changerX(8)

# Changement de la valeur de la coordonnée y
point_instance.changerY(10)

# Affichage des nouvelles coordonnées
point_instance.afficherLesPoints()