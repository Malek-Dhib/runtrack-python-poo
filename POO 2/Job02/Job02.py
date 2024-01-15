class Livre:
    def __init__(self, titre, auteur, nombre_de_pages): 
        self.titre = titre
        self.auteur = auteur
        self.nombre_de_pages = nombre_de_pages

    def getTitre(self):
        return self.titre

    def getAuteur(self):
        return self.auteur

    def getNombrePages(self):
        return self.nombre_de_pages

    # Mutateurs (setters)
    def setTitre(self, nouveau_titre):
        self.titre = nouveau_titre

    def setAuteur(self, nouvel_auteur):
        self.auteur = nouvel_auteur

    def setNombrePages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.nombre_de_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

livre_instance = Livre("Harry Potter", "J.K. Rowling", 500)

# Affichage des valeurs initiales
print(f"Titre : {livre_instance.getTitre()}")
print(f"Auteur : {livre_instance.getAuteur()}")
print(f"Nombre de pages : {livre_instance.getNombrePages()}")

# Modification des valeurs
livre_instance.setTitre("Le Seigneur des Anneaux")
livre_instance.setAuteur("J.R.R. Tolkien")
livre_instance.setNombrePages(700)

# Affichage des nouvelles valeurs
print(f"Nouveau titre : {livre_instance.getTitre()}")
print(f"Nouvel auteur : {livre_instance.getAuteur()}")
print(f"Nouveau nombre de pages : {livre_instance.getNombrePages()}")

# Tentative de modification du nombre de pages avec une valeur invalide
livre_instance.setNombrePages(-100)