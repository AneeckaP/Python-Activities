class Computer:
    def __init__(self,price):
        self.__maxprice=price
    def sell(self):
        print(f"Sold for {self.__maxprice}")
    
    def setMaxPrice(self,amount):
        self.__maxprice=amount
dell=Computer(1000)
dell.sell()
dell.__maxprice=600
dell.sell()
dell.setMaxPrice(1200)
dell.sell()