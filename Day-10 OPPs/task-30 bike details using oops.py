class Bikes():
    def __init__(self, bike_name, bike_cc, millage):
        self.a=bike_name
        self.b=bike_cc
        self.c=millage

    def Bike_Data(self):
        print("Bike Name:", self.a)
        print("Bike CC:", self.b)
        print("Bike Millage:", self.c)





bike_name = input("Enter Bike-1 Name")
bike_cc = input("Enter Bike-1 CC")
millage = input("Enter Bike-1 Millage")
Bike1 = Bikes(bike_name, bike_cc, millage)
Bike1.Bike_Data()




bike_name = input("Enter Bike-2 Name")
bike_cc = input("Enter Bike-2 CC")
millage = input("Enter Bike-2 Millage")

Bike2 = Bikes(bike_name, bike_cc, millage)
Bike2.Bike_Data()