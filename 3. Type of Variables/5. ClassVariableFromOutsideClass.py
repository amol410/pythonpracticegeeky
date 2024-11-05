# Accessing Class Variable from outside Class
class Mobile:
	fp = 'Yes'	# Creating  Class Variable
	
	def __init__(self):
		self.model = 'RealMe X'	# Creating Instance Variable
	
	def show_model(self):		# Instance Method
		print("Model:",self.model)	# Accessing Instance Variable
		
	@classmethod   # Class Method
	def is_fp(cls):
		print("Finger Print:", cls.fp)	# Accessing Class Variable

		
realme = Mobile() #This time nothing will print as no print function in constructor
realme.show_model()
Mobile.is_fp()   # class.classmethod
print()
Mobile.fp = 'No' # class.classvariable # Accessing Class Variable from outside Class
Mobile.is_fp()



