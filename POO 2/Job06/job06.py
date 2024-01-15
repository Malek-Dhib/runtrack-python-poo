class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}
        self._statut_commande = "en cours"

    # Méthode privée pour calculer le total d'une commande
    def _calculer_total(self):
        total = sum(plat["prix"] for plat in self._plats_commandes.values())
        return total

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        self._plats_commandes[nom_plat] = {"prix": prix_plat, "statut": self._statut_commande}
        print(f"Plat '{nom_plat}' ajouté à la commande.")

    # Méthode pour annuler une commande
    def annuler_commande(self):
        self._statut_commande = "annulée"
        print("La commande a été annulée.")

    # Méthode pour afficher la commande avec le total à payer
    def afficher_commande(self):
        total = self._calculer_total()
        print(f"Commande #{self._numero_commande} - Statut: {self._statut_commande}")
        for nom_plat, plat in self._plats_commandes.items():
            print(f"{nom_plat}: {plat['prix']} €")
        print(f"Total à payer : {total} €")

    # Méthode pour calculer la TVA
    def calculer_tva(self, taux_tva):
        total = self._calculer_total()
        tva = total * taux_tva / 100
        print(f"TVA ({taux_tva}%): {tva} €")
        return tva


# Exemple d'utilisation de la classe Commande avec les nouvelles fonctionnalités
commande_instance = Commande("123")

# Ajout de plats à la commande
commande_instance.ajouter_plat("Pizza", 12.5)
commande_instance.ajouter_plat("Salade", 8.75)
commande_instance.ajouter_plat("Pâtes", 10.0)

# Affichage de la commande
commande_instance.afficher_commande()

# Annulation de la commande
commande_instance.annuler_commande()

# Affichage de la commande annulée
commande_instance.afficher_commande()

# Calcul de la TVA
commande_instance.calculer_tva(10)
