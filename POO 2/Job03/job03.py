class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_pages = nombre_pages
        self._disponible = True

    # Assesseurs (getters)
    def getTitre(self):
        return self._titre

    def getAuteur(self):
        return self._auteur

    def getNombrePages(self):
        return self._nombre_pages

    def getDisponible(self):
        return self._disponible

    # Mutateurs (setters)
    def setTitre(self, nouveau_titre):
        self._titre = nouveau_titre

    def setAuteur(self, nouvel_auteur):
        self._auteur = nouvel_auteur

    def setNombrePages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self._nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    # Méthode pour vérifier si le livre est disponible
    def verification(self):
        return self._disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        if self.verification():
            self._disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible.")

    # Méthode pour rendre le livre
    def rendre(self):
        if not self.verification():
            self._disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté.")

# Exemple d'utilisation de la classe Livre avec les nouvelles fonctionnalités
livre_instance = Livre("Harry Potter", "J.K. Rowling", 500)

# Vérification de la disponibilité du livre
print(f"Le livre est disponible : {livre_instance.verification()}")

# Emprunt du livre
livre_instance.emprunter()

# Vérification de la disponibilité après l'emprunt
print(f"Le livre est disponible : {livre_instance.verification()}")

# Tentative d'emprunt du livre déjà emprunté
livre_instance.emprunter()

# Rendre le livre
livre_instance.rendre()

# Vérification de la disponibilité après le rendu
print(f"Le livre est disponible : {livre_instance.verification()}")
