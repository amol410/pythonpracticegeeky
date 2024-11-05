# Class Variable - NameSpace
''' A namespace is a way to organize your code in a neat and organized manner. 
It's like having different rooms in a house, each with its own set of items.'''
class Mobile:
	fp = 'Yes'								# Class Variable which belongs to namespace of Mobile Class
		
	@classmethod							# Class Method
	def is_fp(cls):
		print("Finger Print:", cls.fp)		# Accessing Class Variable

		
realme = Mobile()
redmi = Mobile()
geek = Mobile()

print("Class FP:", Mobile.fp) # class.classvariable
print("RealMe:", realme.fp)   # object.classvariable
print("Redmi:", redmi.fp)
print("Geek:", geek.fp)

print()
Mobile.fp = 'No'	# Modifying Class Variable using Class
print("Class FP:", Mobile.fp)
print("RealMe:", realme.fp)
print("Redmi:", redmi.fp)
print("Geek:", geek.fp)
print()
realme.fp = 'Not Working'	# Modifying Class Variable using object
print("Class FP:", Mobile.fp)
print("RealMe:", realme.fp)
print("Redmi:", redmi.fp)
print("Geek:", geek.fp)
print()



