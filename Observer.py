##################  design
class Observer(object):
    def __init__(self, name):
        self._name = name

    def subscribe(self, subject):
        subject.addObserver(self)
        print self._name + ' subscribe ' + subject.__class__.__name__

    def update(self, subject):
        pass

class Subject(object):
    def __init__(self):
        self._observerList = []
        self._content = ''

    def addObserver(self, observer):
        self._observerList.append(observer)

    def notify(self):
        print self.__class__.__name__ + ' said to all observers: ' + self._content

        for i in self._observerList:
            i.update(self)

    def setContent(self, content):
        self._content = content
        self.notify()

    def getContent(self):
        self._content

################## Concrete class
class News(Subject):
    def getContent(self):
        return self._content + ' from News'

class TV(Subject):
    def getContent(self):
        return self._content + ' from TV'

class Person(Observer):
    def update(self, subject):
        print self._name + ' gets ' + subject.getContent()

################## use case
def main():
    # create subjects
    news = News()
    tv = TV()

    # create observers
    me = Person('David')
    she = Person('Merry')

    # observers subscribe subjects
    me.subscribe(news)
    me.subscribe(tv)

    she.subscribe(news)

    # when subject updates
    news.setContent('today is a good day')
    tv.setContent('we have new TV shows')

if __name__ == '__main__':
    main()
