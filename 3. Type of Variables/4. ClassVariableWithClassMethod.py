# Class Variable or Static Variable with Class Method
class Mobile:
	fp = 'Yes'	# Class Variable
	
	def __init__(self):
		self.model = 'RealMe X'	# Creating Instance Variable
	
	def show_model(self):		   # Instance Method
		print("Model:",self.model) # Accessing Instance Variable
		
	@classmethod # Class Method
	def is_fp(cls):
		print("Finger Print:", cls.fp)	# Accessing Class Variable

		
realme = Mobile() # creating object
realme.show_model() # object.method
Mobile.is_fp() # class.classmethod
