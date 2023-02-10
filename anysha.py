# # import triangle
class Shapes:
    def __init__(self, triangle,rectangle,square,circle,trapezium,rhombus,parallelogram):
        self.rectangle = rectangle
        self.square = square
        self.circle = circle
        self.trapezium = trapezium
        self.rhombus = rhombus
        self.parallelogram = parallelogram
        self.triangle = triangle
def triangle (base, height):
        area = 0.5*base*height
        print("The are of the triangle is",area,"square units")   
def rectangle(length,width):
        area = length*width
        print("The are of the rectangle is",area,"square units")
def Square (width):
        area = widths*widths
        print("The area of the square is",area,"square units")
def Circle (radius):
        area = 3.142*radius*radius
        print("The area of the circle is",area,"square units")
def Trapezium(long_side,short_side, height):
        area = (0.5*(long_side+short_side))*height
        print("The area of the trapezium is",area,"square units")
def Parallelogram (basep,heightp):
        area = basep*heightp
        print("The area of the parallelogram is",area,"square units")
def rhombus (baser,heightr):
        area = baser*heightr
        print("The area of the rhombus is",area,"square units")

print("LET'S CALCULATE YOUR AREA")
print("which shape area do you want to calulate? ")
print("1.triangle")
print("2. rectangle")
print("3. square")
print("4. circle")
print("5. trapezium")
print("6. parallelogram")
print("7. rhombus ")
select = int(input("Enter shape: "))
if select == 1 or 'triangle':
        besa = float(input("Enter base: "))
        hata = float(input("enter height: "))
        triangle(besa, hata)
elif select == 2:
    lengtha = float(input("Enter length : "))
    widtha = float(input("Enter width : "))
    rectangle(lengtha, widtha)
elif select == 3:
     widths = float(input("Enter width : "))
     Square(widths)
elif select == 4:
    radiusa = float(input("Enter radius : "))
    Circle(radiusa)
elif select == 5:
    long_side1 = float(input("Enter length of long side : "))
    short_side1 = float(input("Enter length of short side : "))
    height1t = float(input("Enter Height Value : "))
    Trapezium(long_side1, short_side1, height1t)
elif select == 6:
    basepp = float(input("Enter your base : "))
    heightpp = float(input("Enter your height : "))
    Parallelogram(basepp, heightpp)
elif select == 7:
    baserr = float(input("Enter your base : "))
    heightrr = float(input("Enter your height value : "))
    rhombus(baserr, heightrr)
else:
    print("Invalid input")
    print("Contact +254796871876 for help")

   


