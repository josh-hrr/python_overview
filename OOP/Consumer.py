from Vehicule import Vehicule

class Consumer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicules = []

    def buy_vehicule(self, vehicule: Vehicule):
        if vehicule.check_available():
            vehicule.sell()
            self.purchased_vehicules.append(vehicule)
        else:
            print(f"El vehicule {vehicule.brand} no esta disponible")
    
    def inquire_vehicule(self, vehicule: Vehicule):
        if vehicule.check_available():
            availability = "Disponible"
        else:
            availability = "No Disponible"
        print(f"El {vehicule.brand} esta {availability} y cuesta {vehicule.get_price()}")

