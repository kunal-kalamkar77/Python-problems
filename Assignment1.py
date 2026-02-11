#Problem Statement 1 -Make a program to calculate area of circle, triangle,square, and rectangle. 


#we will use input function here for inputs of dimensions
r = int(input("Enter the radius of circle :"))
area_of_circle = 3.14*(r**2)
print("Area of circle is :",area_of_circle)
b = int(input("Enter the base of triangle :"))
h = int(input("Enter the height of triangle :"))
area_of_triangle = 0.5*b*h
print("Area of triangle is :",area_of_triangle)
s = float(input("Enter the side of square :"))
area_of_square = s**2
print("The area of square is :",area_of_square)
l1 = int(input("Enter the length of rectangle :"))
b1 = int(input("Enter the breadth of rectangle :"))
area_of_rectangle = l1*b1
print("Area of rectangle is :",area_of_rectangle)
