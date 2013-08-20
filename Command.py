##################  design
class Command(object):
    def execute(self):
        pass

class ConcreteCommand(Command):
    def execute(self):
        pass

class Operator(object):
    def action(self):
        pass

class Invoker(object):
    '''
    Invoker act as a command logger and executor
    '''
    def __init__(self):
        self.commandHistory = []

    def invoke(self, command):
        self.commandHistory.append(command)
        command.execute()

    # a candy from this design
    def redo(self):
        if self.commandHistory:
            lastCmd = self.commandHistory.pop()
            lastCmd.execute()

################## Concrete class
class MyCommand(Command):
    def __init__(self, operator, parameter):
        self._receiver = operator
        self._parameter = parameter

    def execute(self):
        # tell the operator to do something
        self._receiver.action(self._parameter)

class Light(Operator):
    def action(self, parameter):
        if 'LP' == parameter:
            print 'Light up'
        elif 'LD' == parameter:
            print 'Light down'

################## use case
def main():
    light = Light()
    lightUpCmd = MyCommand(light, 'LP')
    lightDownCmd = MyCommand(light, 'LD')

    switch = Invoker()
    switch.invoke(lightUpCmd)
    switch.invoke(lightDownCmd)

    switch.redo()
    switch.redo()

if __name__ == '__main__':
    main()