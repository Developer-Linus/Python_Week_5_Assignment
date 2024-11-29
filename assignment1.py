class Laptop:
    # Constructor to initialize attributes
    def __init__(self, model, color, screen_size, serial_no, turned_on):
        self.model = model
        self.color = color
        self.screen_size = screen_size
        self._serial_no = serial_no
        self.turned_on = turned_on
       
    
    # Method to display Laptop properties
    def display_details(self):
        print(f"The model of this laptop is {self.model} with the color {self.color} and screes size {self.screen_size}.")
    
    # Method to check if laptop is powered on or off
    def state(self):
        if(self.turned_on == True):
            print("You can operate your laptop.")
        else:
            print("The laptop is turned off.")
    # Method for getting the serial no
    def _get_Serial(self): #Protected method
        print(f"The laptop serial no: {self._serial_no}")
    
    # Method 
    def purpose(self):
        pass

class Gaming(Laptop):
    def purpose(self):
        return f"This laptop is for installing and running games."
class GeneralPurpose(Laptop):
    def __init__(self, model, color, screen_size, serial_no, turned_on, graphics_card):
        super().__init__(model, color, screen_size, serial_no, turned_on)
        self.graphics_card = graphics_card
    def purpose(self):
        super().display_details()
        if(self.graphics_card == True):
            print(f"This machine is used for gaming and resource-intensive applications.")
        else:
            print(f"Consider looking for another laptop with graphics card to run heavy applications.")
# Instantiating class laptop
my_laptop = Laptop("HP", "Grey", 13, "HT34MHit", True)
my_laptop.display_details()
my_laptop.state()
print(my_laptop._serial_no)

gaming_laptop = GeneralPurpose("HP", "Grey", 13, "HT34MHit", True, True)
gaming_laptop.purpose()






