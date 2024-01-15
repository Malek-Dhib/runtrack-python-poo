class Personne:
    def __init__(self, nom, prénom):
        self.nom = nom
        self.prénom = prénom

    def SePresenter(self):
        return f"Bonjour Je m'appelle {self.prénom} {self.nom}"

Personne1 = Personne("Dur", "Pierre")
Personne2 = Personne("Astral" , "Luc")

print(Personne1.SePresenter())
print(Personne2.SePresenter())