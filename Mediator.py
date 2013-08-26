##################  design
class Mediator(object):
	def __init__(self):
		self._memberDict = {}

	def colleaqueChanged(colleaque):
		pass

	def addMember(self, name, colleaque):
		self._memberDict[name] = colleaque
		colleaque.setMediator(self)

class Colleaque(object):
	def setMediator(self, mediator):
		self._mediator = mediator

	def changed(self):
		self._mediator.colleaqueChanged(self)

	def getValue(self):
		return None

	def setValue(self, value):
		pass

################## Concrete class
class UIMediator(Mediator):
	def colleaqueChanged(self, colleaque):
		print colleaque.getValue()
		print 'which one do you want me to pass the message?'

class TextField(Colleaque):
	def getValue(self):
		return 'value from TextField'

	def setValue(self):
		pass

class Button(Colleaque):
	def getValue(self):
		return 'value from Button'

	def setValue(self):
		pass

class ListBox(Colleaque):
	def getValue(self):
		return 'value from ListBox'

	def setValue(self):
		pass

################## use case
def main():
    mediator = UIMediator()

    button = Button()

    textField = TextField()

    listBox = ListBox()

    mediator.addMember('button', button)
    mediator.addMember('textField', textField)
    mediator.addMember('listBox', listBox)

    button.changed()

    listBox.changed()


if __name__ == '__main__':
    main()
