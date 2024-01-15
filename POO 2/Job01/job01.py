class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur 

    def getLongueur(self):
        return self.longueur

    def getLargeur(self):
        return self.largeur

    def setLongueur(self, nouvelle_longueur):
        self.longueur = nouvelle_longueur

    def setLargeur(self, nouvelle_largeur):
        self.largeur = nouvelle_largeur

rectangle_instance = Rectangle(10, 5)

print(f"Longueur initiale : {rectangle_instance.getLongueur()}")
print(f"Largeur initiale : {rectangle_instance.getLargeur()}")

# Modification de la longueur et de la largeur
rectangle_instance.setLongueur(15)
rectangle_instance.setLargeur(8)

print(f"Nouvelle longueur : {rectangle_instance.getLongueur()}")
print(f"Nouvelle largeur : {rectangle_instance.getLargeur()}")

