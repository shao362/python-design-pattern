
# Python reflection API demo
class Me(object):
    def jump(self):
        print 'jump'

    def sleep(self):
        print 'sleep'

class You(object):
    def laugh(self):
        print 'laugh'

    def walk(self):
        print 'walk'

def getClassByName(className, objList):
    for i in objList:
        if i and className == i.__class__.__name__:
            return i

def createClassByName(className):
    if 'You' == className:
        return You()
    elif 'Me' == className:
        return Me()
    else:
        return None

################## use case
def main():
    me = Me()
    you = You()

    # test to get a class instance by its name
    objList = [me, you]
    anotherYou = getClassByName('You', objList)   
    print type(you)
    print type(anotherYou)

    # test to create a class instance by its name
    anotherMe = createClassByName('Me')
    print type(anotherMe)

    # test if attribute is callable
    for i in dir(me):
        if callable(getattr(me, i)):
            print i + ' is callable'
        else:
            print i + ' is not callable'

    # get class name
    print me.__class__.__name__

if __name__ == '__main__':
    main()
