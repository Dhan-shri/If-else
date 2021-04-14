a=int(input("enter first num:-"))
b=int(input("enter sec number:-"))
c=int(input("enter third number:-"))
if (a>b and b>c) or (a<b and b<c):
    print(b)
elif (b>c and c>a) or (b<c and c<a):
    print(c)
else:
    print(a)