from Vehicule import Vehicule
from Consumer import Consumer

class Dealership:
    def __init__(self):
        self.inventory = []
        self.consumers = []
    
    def add_vehicules(self, vehicule: Vehicule):
        self.inventory.append(vehicule)
        print(f"El {vehicule.brand} ha sido a;adido al invetario")

    def register_consumers(self, consumer: Consumer):
        self.consumers.append(consumer)
        print(f"El cliente {consumer.name} ha sido a;adido")
    
    def show_available_vehicule(self):
        print(f"Vehicules disponibles en la tienda")
        for vehicule in self.inventory:
            if vehicule.check_available():
                print(f"- {vehicule.brand} por {vehicule.get_price()}")