"""
Project 3 Description

Create a Python class Triangle.
Each instance of this class takes 6 values Ax,Ay,Bx,By,Cx,Cy as arguments that represent the (x,y) coordinates for three points A, B, and C.
In addition, overload the str() function so that we can print the triangle as "Triangle((Ax,Ay),(Bx,By),(Cx,Cy))"
and create the following methods:
Area, which returns the area of a triangle,
Perimeter, which returns the perimeter of a triangle,
Barycenter, which returns the center of a triangle,
LongestSide, which returns the length of the longest side in the triangle,
and IsRightTriangle, which returns True if a triangle is a right triangle or False if it is not a right triangle.


In your .txt version of the report, include the Python code and the output returned by all methods
for the triangle T, given by the points A = (3, -5), B = (15, 4), C = (-6,10).
"""
import math

class Triangle(object):

    def __init__(self,Ax,Ay,Bx,By,Cx,Cy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy

    def __str__(self):
        return "Triangle(%f,%f,%f,%f,%f,%f)" % (self.Ax,self.Ay,self.Bx,self.By,self.Cx,self.Cy)

    def side_length(self):

        side1 = math.sqrt((self.Ax - self.Bx)**2 + (self.Ay - self.By)**2) #AB
        side2 = math.sqrt((self.Ax - self.Cx)**2 + (self.Ay - self.Cy)**2) #AC
        side3 = math.sqrt((self.Bx - self.Cx)**2 + (self.By - self.Cy)**2) #BC
        return [side1,side2,side3] #say self.side_length[0]



    def area(self):
        #herons formula
        S = (self.side_length())
        A = S[0]
        B = S[1]
        C = S[2]
        return (.25)*math.sqrt((A+B+C)*(-A+B+C)*(A-B+C)*(A+B-C))

    def perimeter(self):
        #sideA+sideB+sideC
        S = self.side_length()
        triangleperimeter =  S[0]+S[1]+S[2]
        return triangleperimeter

    def barycenter(self):
        #ave x, ave y
        centerx = (self.Ax+self.Bx+self.Cx)
        centery = (self.Ay+self.By+self.Cy)
        return centerx,centery

    def longest_side(self):
        #return max
        S = (self.side_length())
        A = S[0]
        B = S[1]
        C = S[2]
        return max(A,B,C)


    def is_right_triangle(self):
        #return true/false
        S = (self.side_length())
        A = S[0]
        B = S[1]
        C = S[2]
        e = 0.00000001
        if abs((A**2)+(B)**2 - (C)**2) < e:
            return True
        elif abs((B**2)+(C**2)-(A**2)) < e:
            return True
        elif abs((C**2)+(A**2)-(B**2)) < e:
            return True
        else:
            return False






def main():
    T1 = Triangle(3,-5,15,4,-6,10)
    print(type(T1.side_length()))
    print(T1.area())
    print(T1.perimeter())
    print(T1.barycenter())
    print(T1.longest_side())
    print(T1.is_right_triangle())


main()