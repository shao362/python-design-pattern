
STATE_A = 'A'  # start state
STATE_B = 'B'
STATE_C = 'C'
STATE_D = 'D'
STATE_END = 'END'

##################  design
class Handler(object):
    def process(self):
        pass

class StateMachine(object):
    def __init__(self):
        self.currentState = STATE_END
        self.handlerList = {}

    def addState(self, state, handler):
        self.handlerList[state] = handler

    def start(self):
        nextState = STATE_A  # start state
        while(STATE_END != nextState):
            handler = self.handlerList.get(nextState, None)
            if handler:
                nextState = handler.process()
            else:
                nextState = STATE_END

################## Concrete class
class HandlerA(Handler):
    def process(self):
        print 'processing state A'
        return STATE_B

class HandlerB(Handler):
    def process(self):
        print 'processing state B'
        return STATE_C

class HandlerC(Handler):
    def process(self):
        print 'processing state C'
        return STATE_D

class HandlerD(Handler):
    def process(self):
        print 'processing state D'
        return STATE_END

################## use case
def main():
    '''
    A -> B -> C -> D -> END
    '''
    sm = StateMachine()

    sm.addState(STATE_A, HandlerA())
    sm.addState(STATE_B, HandlerB())
    sm.addState(STATE_C, HandlerC())
    sm.addState(STATE_D, HandlerD())

    sm.start()

if __name__ == '__main__':
    main()
