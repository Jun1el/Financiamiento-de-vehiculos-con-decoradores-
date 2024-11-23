class AccessoryDecorator:
    """Clase base para los accesorios decoradores."""
    def __init__(self, vehicle):
        self._vehicle = vehicle

    def get_description(self):
        return self._vehicle.get_description()

    def get_cost(self):
        return self._vehicle.get_cost()


class AirConditioning(AccessoryDecorator):
    def get_description(self):
        return self._vehicle.get_description() + ", Aire Acondicionado"

    def get_cost(self):
        return self._vehicle.get_cost() + 1500


class LeatherSeats(AccessoryDecorator):
    def get_description(self):
        return self._vehicle.get_description() + ", Asientos de Cuero"

    def get_cost(self):
        return self._vehicle.get_cost() + 2000


class SoundSystem(AccessoryDecorator):
    def get_description(self):
        return self._vehicle.get_description() + ", Sistema de Sonido Premium"

    def get_cost(self):
        return self._vehicle.get_cost() + 1200
