
class Rectangle:

    def __init__(self):
        self.length = 5
        self.width = 5
        

    def set_length(self, l):
        self.length = l


    def set_width(self, w):
        self.width = w


    def get_length(self, w):
        return self.length


    def get_width(self, w):
        return self.width

    
    def area(self):
        return (self.length * self.width)

    def premieter(self):
        return (self.length + self.width) * 2
        
        
        

