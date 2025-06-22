class IOString():
    def __init___(self):
        self=str1=""
    def getString(self):
        self.str1=input("Enter String:")
    def printString(self):
        print(f"The result is: {self.str1.upper()}")

str1=IOString()
str1.getString()
str1.printString()