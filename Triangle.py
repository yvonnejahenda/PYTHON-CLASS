class Triangle:
 base=0
 height=0
 hypotenuse=0
 
 def __init__(self,base,height):
   self.base=base
   self.height=height
   
 def area (self):
    return 0.5*self.base * self.height
    
 def perimeter (self):
    return self.base+self.height+self.hypotenuse
    
 small=Triangle (2,3,)
 large=Triangle (200,300,400)
 print=("base and height of smaller {} {}".format (small.base,small.height))
 print(larger.area,large.area())