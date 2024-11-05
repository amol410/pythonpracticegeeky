# Accessing Instance Variable from Outside Class
class Mobile:
	def __init__(self):
		self.model = 'RealMe X' # Creating Instance Variable
	
	def show_model(self): # Instance Method
		print(self.model) # Accessing Instance Variable Inside Class

		
realme = Mobile()
realme.show_model()
# Accessing Instance Variable from Outside Class
r = realme.model # object.instancevariable
print("Outside Class:", r)	
