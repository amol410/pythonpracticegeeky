# Instance Variable
class Mobile:
	def __init__(self):
		self.model = 'RealMe X'	# Creating Instance Variable
	
	def show_model(self): # Instance Method
		print(self.model) # Accessing Instance Variable

		
realme = Mobile()
redmi = Mobile()
geek = Mobile()

print("RealMe:", realme.model) # object.instancevariable
print("Redmi:", redmi.model)   # object.instancevariable
print("Geek:", geek.model)     # object.instancevariable
print()
redmi.model = 'Redmi 7s'  # Modifying Instance Variable
print("RealMe:", realme.model)
print("Redmi:", redmi.model)
print("Geek:", geek.model)
