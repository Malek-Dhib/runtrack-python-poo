class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._credits = 0
        self._level = self._studentEval()

    # Méthode privée pour évaluer le niveau de l'étudiant
    def _studentEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Assesseurs (getters)
    def getNom(self):
        return self._nom

    def getPrenom(self):
        return self._prenom

    def getNumeroEtudiant(self):
        return self._numero_etudiant

    def getCredits(self):
        return self._credits

    def getLevel(self):
        return self._level

    # Mutateur (setter) pour ajouter des crédits
    def addCredits(self, nombre_credits):
        if nombre_credits > 0:
            self._credits += nombre_credits
            self._level = self._studentEval()
            print(f"{nombre_credits} crédits ajoutés avec succès.")
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    # Méthode pour afficher les informations de l'étudiant
    def studentInfo(self):
        print(f"Informations de l'étudiant {self._prenom} {self._nom} ({self._numero_etudiant}):")
        print(f"Nom : {self._nom}")
        print(f"Prénom : {self._prenom}")
        print(f"Numéro étudiant : {self._numero_etudiant}")
        print(f"Nombre de crédits : {self._credits}")
        print(f"Niveau : {self._level}")

# Exemple d'utilisation de la classe Student avec les nouvelles fonctionnalités
john_doe = Student("Doe", "John", 145)

john_doe.addCredits(32)
john_doe.addCredits(28)
john_doe.addCredits(30)
john_doe.studentInfo()
