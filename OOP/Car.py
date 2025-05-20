from Vehicule import Vehicule

class Car(Vehicule):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no esta disponible"