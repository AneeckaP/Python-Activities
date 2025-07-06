class MyClass:
    name="Aneecka"
    __money=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

    def info(self):
        print(f"Name: {self.name}")
        print(f"Money: {self.__money}")
aneecka=MyClass()
aneecka.info()
aneecka.name="Aneecka Pallikonda"
aneecka.info()
aneecka.__money=1200000000000000000000
aneecka.info()