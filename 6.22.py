a = int(input())
b = int(input())
c = int(input())
a1 = int(input())
b1 = int(input())
c1 = int(input())
flag = False
for x in range(-10,11):
    for y in range(-10,11):
        if a*x+b*y-c==0 and a1*x+b1*y-c1==0:
            print(x,y)
            flag = True

if flag == False:
    print('No solution')