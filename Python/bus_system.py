class Bus:
    places = ['Tampines', 'Bedok', 'Kallang', 'Downtown', 'Clementi']
    
    def __init__(self, place1, place2, places=places):
        self.place1 = places.index(place1)
        self.place2 = places.index(place2)

    def calculateFare(self):
        difference = self.place2 - self.place1
        fare = abs(difference) * 0.5
        print("Total station:", difference, end=' | ')
        print("Total fare: $", fare)


bus1 = Bus("Bedok", "Downtown")
bus1.calculateFare()

bus1 = Bus("Tampines", "Clementi")
bus1.calculateFare()