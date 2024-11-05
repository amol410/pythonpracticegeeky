# Instance Variable with Instance Method
class Mobile:
	def __init__(self): # constructor method
		self.model = 'RealMe X'	# Creating Instance Variable
	
	def show_model(self): # Instance Method
		print(self.model) # Accessing Instance Variable

		
realme = Mobile() # object created without argument
realme.show_model() # object.method
	
