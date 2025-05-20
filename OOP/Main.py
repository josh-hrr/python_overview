from Car import Car
from Bike import Bike
from Truck import Truck
from Consumer import Consumer
from Dealership import Dealership

class Main:
    print("this is a test")
    
    car1 = Car("Toyota", "Yaris", 160000)
    bike1 = Bike("Yamaha", "MT-07", 7000)
    truck1 = Truck("Volvo", "FH16", 80005)

    consumer1 = Consumer("Joshua")

    dealership1 = Dealership()
    dealership1.add_vehicules(car1)
    dealership1.add_vehicules(bike1)
    dealership1.add_vehicules(truck1)

    #Show available vehicules
    dealership1.show_available_vehicule()

    #Consumer looks for a vehicule
    consumer1.inquire_vehicule(car1)

    #Consumer buys the vehicule
    consumer1.buy_vehicule(car1)

    #Show available vehicules
    dealership1.show_available_vehicule()
    #Consumer buys the vehicule
    consumer1.buy_vehicule(car1)

    #Show available vehicules
    dealership1.show_available_vehicule()



