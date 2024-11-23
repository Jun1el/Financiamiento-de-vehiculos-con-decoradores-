class BaseVehicle:
    """Clase base para vehículos."""
    def __init__(self,cost):
        self.description = "Vehículo Base"
        self.cost = cost  # Costo base del vehículo

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
