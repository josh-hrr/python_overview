from Vehicule import Vehicule

class Bike(Vehicule):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del la bike {self.brand} esta en marcha"
        else:
            return f"La bike {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor de la bike {self.brand} se ha detenido"
        else:
            return f"La bike {self.brand} no esta disponible"