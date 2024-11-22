from abc import ABC, abstractmethod
class polygon :
    
    def info(self):
        print("polygon represent the two dimension figure")

    @abstractmethod
    def area(self,side1,side2):
        pass

class rectangle(polygon):

    def rect_info(self):
        print("Rectangle are made up of for sides ")

    def area(self, side1,side2):
        
        result = side1*side2
        print("Area of Rectangle = ",result)

class triangle(polygon):
    def tri_info(self):
        print("Triangle are made up of thee sides")

    def area(self,base,height):
        result = (base*height)/2

rect1= rectangle()
rect1.info()
rect1.rect_info()
rect1.area(5,6)

        