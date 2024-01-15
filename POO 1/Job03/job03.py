class Operation:
    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3

    def addition(self):
        result = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition est : {result}")

# Instanciation de la classe
operation_instance = Operation()

# Appel de la méthode addition
operation_instance.addition()