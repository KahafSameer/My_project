class car:
    def __init__(self,brand,color,size,wheel):
        self.brand=brand
        self.color=color 
        self.size=size
        self.wheel=wheel
    def describe(self):
        print("there is my new",self.brand,"its colour is",self.color,"its a",self.size,"car""it has",self.wheel,"wheel")

mycar=car("BMW","BLACK","LARGE","4")
mycar.describe()