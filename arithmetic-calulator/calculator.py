class Calculator:
    def __init__(self, number_one, number_two):
        self.one = number_one
        self.two = number_two
    
    def add(self):
        print(self.one + self.two)
    
    def subtract(self):
        print(self.one - self.two)
    
    def multiply(self):
        print(self.one * self.two)
    
    def divide(self):
        # Attempt to catch division by zero error
        try:
            print(self.one / self.two)
        except ZeroDivisionError:
            print("0")