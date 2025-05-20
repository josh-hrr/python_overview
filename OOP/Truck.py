from Vehicule import Vehicule

class Truck(Vehicule):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del Truck {self.brand} esta en marcha"
        else:
            return f"El Truck {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del Truck {self.brand} se ha detenido"
        else:
            return f"El Truck {self.brand} no esta disponible"
