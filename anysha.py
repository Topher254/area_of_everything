class Shapes:
    def __init__(self, triangle,rectangle,square,circle,trapezium,rhombus,parallelogram):
        self.rectangle = rectangle
        self.square = square
        self.circle = circle
        self.trapezium = trapezium
        self.rhombus = rhombus
        self.parallelogram = parallelogram
        self.triangle = triangle
    def Triangle (self):
        base = input("Enter base : ")
        height = input("Enter Height")
        area = 0.5*base*height
        print("The are of the triangle is",area,"square units")
    def rectangle(self):
        length = input("Enter length : ")
        width = input("Enter width : ")
        area = length*width
        print("The are of the rectangle is",area,"square units")
    def Square (self):
        width = input("Enter width : ")
        area = lwidth*width
        print("The are of the square is",area,"square units")
    def Circle (self):
        radius = input("Enter radius : ")
        area = 3.142*radius*radius
        print("The are of the rcircle is",area,"square units")
    def Trapezium(self):
        long_side = input("Enter length of long side : ")
        short_side = input("Enter length of short side : ")
        height = input("Enter Height Value : ")
        area = (0.5(long_side+short_side))*height
    def parallelogram (self):
        base = input("Enter your base : ")
        height = input("Enter your height : ")
        area = base*height
    def rhombus (self):
        base = input("Enter your base : ")
        height = input("Enter your height value : ")
        area = base*height

print("LET'S CALCULATE YOUR AREA")
print("which shape area do you want to calulate? ")
print("1.triangle")
print("2. rectangle")
print("3. square")
print("4. circle")
print("5. trapezium")
print("6. rhombus")
print("7. parallelogram ")
answer = input("Enter 1 for triangle, 2 for rectangle e.t.c ... : ")
if answer ==1:
    Triangle()

