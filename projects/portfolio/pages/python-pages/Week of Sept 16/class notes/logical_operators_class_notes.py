a = 10
b = 20
c = 30


if a > b and a > c:
    print("a is the largest number")
elif b > a and b > c:
    print("b is the largest number")
else:
    print("c is the largest number")

if a > b or a > c:
    print("a is the largest number")
elif b > a or b > c:
    print("b is the largest number")
else:
    print("c is the largest number")

if not a > b:
    print("a is not the largest number")
else:
    print("a is greater than b")
