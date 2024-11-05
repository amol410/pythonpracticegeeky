# # Method Overriding
# # Method with Super Method
# class Add:
# 	def result(self, a, b):
# 		print('Addition:', a+b)
		
# class Multi(Add):
# 	def result(self, a, b):
# 		super().result(10, 20)				# Calling Parent Class's Method
# 		print('Multiplication:', a*b)
		
# m = Multi()
# m.result(10, 20)






class add:
    def result(self, a, b):
	    print(a+b)	

class main(add):
    def result(self, a, b):
           super().result(a,b)
           return a*b


x = main()
y= x.result(5,6)
print(y)
