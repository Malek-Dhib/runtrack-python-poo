class Produit:
    def __init__(self, nom, prixHT, tva):
        self.nom = nom
        self.prixHT = prixHT
        self.tva = tva

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.tva / 100)

    def afficher(self):
        infos = f"Nom: {self.nom}, Prix HT: {self.prixHT}€, TVA: {self.tva}%"
        print(infos)

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.tva

# Exemple d'utilisation de la classe Produit
produit1 = Produit("Batterie", 50, 20)
produit2 = Produit("écran", 30, 10)

# Affichage des informations initiales
produit1.afficher()
produit2.afficher()

# Calcul des prix TTC
prix_ttc_produit1 = produit1.calculerPrixTTC()
prix_ttc_produit2 = produit2.calculerPrixTTC()
print(f"Prix TTC Batterie : {prix_ttc_produit1}€")
print(f"Prix TTC écran : {prix_ttc_produit2}€\n")

# Modification du nom et du prix des produits
produit1.modifierNom("Nouveau Produit batterie")
produit1.modifierPrixHT(60)
produit2.modifierNom("Nouveau Produit écran")
produit2.modifierPrixHT(40)

# Affichage des nouvelles informations
produit1.afficher()
produit2.afficher()

# Affichage des nouvelles informations en utilisant les méthodes d'obtention
print(f"Nom du Produit A : {produit1.obtenirNom()}")
print(f"Prix HT du Produit A : {produit1.obtenirPrixHT()}€")
print(f"TVA du Produit A : {produit1.obtenirTVA()}%")
