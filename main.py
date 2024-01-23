class Recurso:
    def __init__(self, x):
        self.x = x
        print(f"proceso {self.x} se ha inicializado.")
    def __del__(self):
        print(f"Proceso {self.x} se han liberado.")
mi_recurso = Recurso(393)
del mi_recurso
class User:
    def __init__(self,user):
        self.user = user
        print(f"El codigo {self.user} se ha ejecutado. ")
    def __del__(self):
        print(f"El codigo {self.user} se ha liberado.")

mi_rec = User(666)
del mi_rec