class Stadium:
    number_of_stadiums = 0

    def __init__(self, name="N/A", location="N/A", capacity=0, opened="N/A", owner="N/A", illuminance=0):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.opened = opened
        self.owner = owner
        self.illuminance = illuminance
        Stadium.number_of_stadiums += 1

    def __del__(self):
        Stadium.number_of_stadiums -= 1

    def __str__(self):
        return "Stadium name: {} \nLocation: {} \nCapacity: {} \nOpened: {} \nOwner: {} \nIlluminance: {} lux \n". \
            format(self.name, self.location, self.capacity, self.opened, self.owner, self.illuminance)

    def display_info(self):
        print(self.__str__())

    @staticmethod
    def get_number_of_stadiums():
        return Stadium.number_of_stadiums


def main():
    theO2 = Stadium("The O2 Arena", "London, UK", 20000, "24 June 2007", "Homes and Communities Agency", 12000)
    theO2.display_info()

    madisonSquareGarden = Stadium("Madison Square Garden", "NYC, NY, USA", opened="11 February 1968",
                                  owner="Madison Square Garden Entertainment")
    madisonSquareGarden.display_info()

    arenaLviv = Stadium("Arena Lviv", "Lviv, Ukraine", 34915)
    arenaLviv.display_info()

    print("Stadiums in base: " + str(Stadium.get_number_of_stadiums()))


if __name__ == "__main__":
    main()

