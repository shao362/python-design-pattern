##################  design
class Handler(object):
    def execute(self, request):
        pass

    def canHandle(self, request):
        return False

class Request(object):
    def __init__(self, value):
        self._value = value

    def getValue(self):
        return self._value

class Invoker(object):
    def __init__(self):
        self.handlerList = []

    def addHandler(self, handler):
        self.handlerList.append(handler)

    def invoke(self, request):
        isHandled = False
        for i in self.handlerList:
            if i.canHandle(request):
                i.execute(request)
                isHandled = True
                break

        if not isHandled:
            print 'Sorry, no one can fulfil this request'

        return isHandled

################## Concrete class
class makeStory(Handler):
    def execute(self, request):
        print 'I will make a story'

    def canHandle(self, request):
        theRequest = request.getValue()
        if 'makeStory' == theRequest:
            return True
        return False

class makeScene(Handler):
    def execute(self, request):
        print 'I will make the scene'

    def canHandle(self, request):
        theRequest = request.getValue()
        if 'makeScene' == theRequest:
            return True
        return False

class startFilming(Handler):
    def execute(self, request):
        print 'Lets start filming'

    def canHandle(self, request):
        theRequest = request.getValue()
        if 'filming' == theRequest:
            return True
        return False

################## use case
def main():
    director = Invoker()

    director.addHandler(makeStory())
    director.addHandler(makeScene())
    director.addHandler(startFilming())

    # client says
    director.invoke(Request('makeScene'))
    director.invoke(Request('makeStory'))
    director.invoke(Request('filming'))
    director.invoke(Request('cancel'))

if __name__ == '__main__':
    main()