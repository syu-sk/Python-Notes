'''Tutorial 9'''

#Task 1 & 2
class Thing:

	def __init__(self, name):
		self.name = name 
		self.owner = None
		self.place = None

	def is_owned(self):
		return self.owner != None

	def get_owner(self):
		return self.owner

	def get_name(self):
		return self.name 

	def get_place(self):
		return self.place

#Task 3
class MobileObject(NamedObject):

    def __init__(self, name, place):
        super().__init__(name)
        self.place = place

    def get_place(self):
        return self.place

#Thing will not inherit from any superclass. MobileObject is not referenced during initialisation of Thing. 
#Correction: replace self.name with super().__init__(name, None)
#calling super() will initialise this object using MobileObject's initialisation method, thus inheriting from it.
