def type(a, b, c):
    if a == b and b == c:
        print('This triangle is equilateral')
    elif a == b or a == c or b == c:
        print('This triangle is isosceles')
    else: 
        print("This triangle is versatile")

print("\nInsert values for the triangle, please: \n")
a = int(input())
b = int(input())
c = int(input())
if (a<=0) or (b<=0) or (c<=0):
    print("Try values > 0")
else:
    if (a+b>c) and (a+c>b) and (c+b>a):#so weak(((
        type(a, b, c)
    else:
        print("sry, but such triangle doesn't exist")

