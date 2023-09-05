print("\nInsert values for the triangle, please: \n")
a = int(input())
b = int(input())
c = int(input())
if (a<=0) or (b<=0) or (c<=0):
    print("Try values > 0")
else:
    if (a+b>c) or (a+c>b) or (c+b>a):
        print("exists")
    else:
        print("sry, but such triangle doesn't exist")

