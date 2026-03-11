class Vehiculo:

    def __init__(self, placa, marca, propietario):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    def obtener_datos(self):
        return (self.placa, self.marca, self.propietario)