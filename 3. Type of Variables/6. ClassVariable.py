# Class Variable
class Mobile:
	fp = 'Yes'	 # Class Variable
		
	@classmethod # Class Method
	def is_fp(cls):
		print("Finger Print:", cls.fp)	# Accessing Class Variable

		
realme = Mobile() # object creation 
redmi = Mobile()  # object creation 
geek = Mobile()   # object creation

print("RealMe:", Mobile.fp) # class.classvariable
print("Redmi:", Mobile.fp)  # class.classvariable
print("Geek:", Mobile.fp)   # class.classvariable
print()
Mobile.fp = 'No'            # Modifying Class Variable
print("RealMe:", Mobile.fp)
print("Redmi:", Mobile.fp)
print("Geek:", Mobile.fp)



