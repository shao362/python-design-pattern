
##################  design
class Product(object):
    def openBox(self):
        pass

class ConcreteProduct(Product):
    def openBox(self):
        print 'Welcome to use this product!'

class Factory(object):
    def __init__(self):
        # prepare products you want to manufacture
        self.productList = {}

        self.addNewProduct('Car', Car)
        self.addNewProduct('Laptop', Laptop)
        self.addNewProduct('Airplane', Airplane)

    def addNewProduct(self, productName, productClass):
        self.productList[productName] = productClass

    def createProductLikePro(self, youNameIt):
        '''
        Factory create a product instance
        '''
        if youNameIt in self.productList:
            return self.productList[youNameIt]()
        return None

    # Simple implementation
    def createLaptop(self):
        return Laptop()

    def createCar(self):
        return Car()

################## Concrete class
class Laptop(Product):
    def openBox(self):
        print 'Welcome to use this Laptop!'

class Car(Product):
    def openBox(self):
        print 'Welcome to use this car!'

class Airplane(Product):
    def openBox(self):
        print 'Welcome to use this Airplane!'

################## use case
class Client:
    def __init__(self):
        self.myShop = Factory()

    def buyCar(self):
        print 'client bought a car'
        car = self.myShop.createCar()
        car.openBox()

    def buyLaptop(self):
        print 'client bought a laptop'
        laptop = self.myShop.createLaptop()
        laptop.openBox()

    def buyAirplane(self):
        print 'client bought an Airplane'
        airplane = self.myShop.createProductLikePro('Airplane')
        if airplane:
            airplane.openBox()

def main():
    client = Client()
    client.buyCar()
    client.buyLaptop()
    client.buyAirplane()

if __name__ == '__main__':
    main()
