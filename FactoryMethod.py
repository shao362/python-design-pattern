##################  design
class Product(object):
    def cloneIt(self):
        '''
        Factory Method abstracts the clone process
        '''
        pass

################## Concrete class
class Car(Product):
    def cloneIt(self):
        return Car()

################## use case
def main():
    car = Car()
    print type(car)
    print id(car)

    anotherCar = car.cloneIt()
    print type(anotherCar)
    print id(anotherCar)

if __name__ == '__main__':
    main()