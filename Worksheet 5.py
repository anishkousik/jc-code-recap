#Set 1
#Written assignment

#Set 2

import math

class LONGINT():
    def __init__(self):
        self._value = 0
        self._sign = "+"
        return
    def getValue(self):
        if self._sign == "+":
            return self._value
        else:
            return self._value*(-1)
    def setValue(self,val):
        val = int(val)
        if val < 0:
            self._sign = "-"
            val *= -1
            self._value = val
            return True
        else:
            self._sign = "+"
            self._value = val
            return True
    def add(self,LONGINT):
        return int(self.getValue()) + int(LONGINT.getValue())
    def subtract(self,LONGINT):
        return int(self.getValue()) - int(LONGINT.getValue())
    def multiply(self,LONGINT):
        return int(self.getValue()) * int(LONGITN.getValue())
    def divide (self,LONGINT):
        return int(self.getValue()) / int(LONGINT.getValue())
    def quotient(self,LONGINT):
        return int(self.getValue()) // int(LONGINT.getValue())
    def modulo(self,LONGINT):
        return int(self.getValue()) % int(LONGINT.getValue())
    def power(self,LONGINT):
        return int(self.getValue())**int(LONGINT.getValue())
    def factorial(self):
        return math.factorial(self.getValue())


a = LONGINT()
#print(a.setValue(11))

b = LONGINT()
b.setValue(5)

#print("a is " + str(a.getValue()))
#print("b is " + str(b.getValue()))
#print(a.divide(b))
#print(a.quotient(b))
#print(a.modulo(b))
#print(a.power(b))
#print(a.factorial())

#Set 3

class Rectangle():
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*self.length + 2*self.breadth

class Square(Rectangle):
    def __init__(self,length):
        self.length = length
        self.breadth = length

class Parallelogram(Rectangle):
    def __init__(self,length,breadth,height):
        super().__init__(length,breadth)
        self.height = height
    def area(self):
        return self.breadth * self.height
    
class Rhombus(Square):
    def __init__(self,d1,d2,length):
        super().__init__(length)
        self.d1 = d1
        self.d2 = d2
    def area(self):
        return (self.d1 * self.d2) / 2

class Kite(Rhombus):
    def __init__(self,d1,d2,length,breadth):
        super().__init__(d1,d2,length)
        self.breadth = breadth

class Trapezium():
    def __init__(self,a,b,c,d,height):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.height = height
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        return ((self.a + self.b) / 2) * self.height

b = Trapezium(2,4,6,8,10)

print(b.area())
print(b.perimeter())
