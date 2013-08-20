################## design
class AbstractFactory(object):
    '''
    Abstract Factory abstracts Factory...
    '''
    def createCar(self):
        pass

    def createLaptop(self):
        pass

    def createProductLikePro(self, youNameIt):
        pass

################## Concrete class
class ToyFactory(AbstractFactory):
    def createCar(self):
        print 'create a toy car'

    def createLaptop(self):
        print 'create a toy laptop'

    def createProductLikePro(self, youNameIt):
        print 'create a toy ' + youNameIt

class MilitaryFactory(AbstractFactory):
    def createCar(self):
        print 'create a tank'

    def createLaptop(self):
        print 'create a robot'

    def createProductLikePro(self, youNameIt):
        print 'create a REAL ' + youNameIt

################## use case
def main():
    toyFactory = ToyFactory()
    toyFactory.createCar()
    toyFactory.createProductLikePro('airplane')

    milFactory = MilitaryFactory()
    milFactory.createCar()
    milFactory.createProductLikePro('airplane')

if __name__ == '__main__':
    main()