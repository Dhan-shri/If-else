num=int(input("side1 of triangle"))
num1=int(input("side2 of triangle"))
num2=int(input("side3 of triangle"))
if num==num1==num2:
    print("it is an equilateral triangle ")
elif num==num1!=num2 or num!=num1==num2 or num==num2!=num1:
    print("it is isosceles triangle")
else:
    print("it is a scelen triangle")
    