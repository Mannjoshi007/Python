class Airline_Reservation:
    formType = "Airline Reservation Form"

    def printData(self):
        print(f'The name of the traveller is {self.name}.')
        print(f'The flight for {self.name} is {self.flight}.')


John=Airline_Reservation()
John.name="John"
John.flight="Continental Terrain"
John.printData()
