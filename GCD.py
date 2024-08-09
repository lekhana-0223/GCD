a=int(input())
b=int(input())
if a == 0 or b == 0:
    print("values must be zero")
else:
    while b:
        a,b=b,a%b
    print(a)
