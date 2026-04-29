class BMW:
    def Fuel(self):
        print("Fuel of BMW is petrol")
    def Speed(self):
        print("Speed of BMW is 270 KM/PH")
class Ferrari:
    def Fuel(self):
        print("Fuel of Ferrari is Disel")
    def Speed(self):
        print("Speed of Ferrari is 300 KM/PH")
t = BMW()
u = Ferrari()

for i in (t, u):
    i.Fuel()
    i.Speed()