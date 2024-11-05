class Mobile:
    def __init__(self):
        self.model = 'RealMe X'    # Instance Variable

    def show_model(self, p):       # Instance Method with Parameter
        price = p                 # Creating a local variable called 'price'
        # Accessing Instance Variable
        print("Model:", self.model, "Price:", price)


# Creating an instance of the Mobile class
realme = Mobile()

# Calling the show_model method with price as a parameter
realme.show_model(1000)

# Accessing price directly
# This will raise a NameError because price is only defined within the method scope
try:
    print(realme.price)
except NameError as e:
    print("NameError:", e)
