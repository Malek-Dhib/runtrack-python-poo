class Animal:
    def __init__(self):
        self.age = 0
        self.nom = ""

    def naissance(self):
        print(f"L'animal est né il a {self.age} ans")

    def viellir(self):
        self.age = self.age + 1
        print(f"L'age de l'animal est de {self.age} ans")

    def nommer(self, nom):
        print(f"L'animal se nomme {nom}")

Age_Nom_Animal = Animal()

Age_Nom_Animal.naissance()
Age_Nom_Animal.viellir()
Age_Nom_Animal.nommer("Martin")
