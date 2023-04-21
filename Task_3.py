class overloading():
    def __init__(self,x,y,z=None) -> None:
        self.x,self.y,self.z = x,y,z
    
    def area(self) -> str:
        if self.x and self.y and self.z:
            return f"ფიგურის მოცულობაა: {self.x * self.y * self.z}"
        elif self.x and self.y:
            return f"ფიგურის ფართობია: {self.x*self.y}"
        else:
            return "Error"
x4 = overloading(5,6,7)
print(x4.area())