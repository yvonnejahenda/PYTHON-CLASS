class Rectangle:
  length = 0
  width = 0
  
  def __init__(self,length,width):
    self.length = length
    self.width = width
    
  def area (self):  
      return self.length *self.width
      
  def perimeter (self):
    return 2*(self.length+self.width)
    
small = Rectangle (2,3)
large=Rectangle(5000,5000)
print("Length and Width of smaller {} and {}".format(small.length,small.width))
print("Smaller area",small.area())
print("larger area",large.area())