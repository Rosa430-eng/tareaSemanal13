class GarajeServicio:

    def __init__(self):
        self.lista_vehiculos = []

    def registrar(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)

    def listar(self):
        return self.lista_vehiculos