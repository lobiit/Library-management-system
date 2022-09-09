x =int(input())
a = 0
b=1
if x == 0:
    print(0)
elif x==1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(1, x):
        c = a + b
        a = b
        b = c
        print(b)