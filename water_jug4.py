from random import randint
print("Water Jug Problem")
xcap=int(input('Enter capacity of x:'))
ycap=int(input('Enter capacity of y:'))
x=int(input("Enter initial X:"))
y=int(input("Enter initial Y:"))
xf=int(input('Enter goal state of x:'))
yf=int(input('Enter goal state of y:'))
while True:
    rno=int(randint(1,10))
    if rno==1:
        if x<xcap:
            x=xcap
    if rno==2:
        if y<ycap:
            y=ycap
    if rno==5:
        if x>0:
            x=0
    if rno==6:
        if y>0:
            y=0
    if rno==7:
        if x+y>=xcap and y>0:
            x,y=xcap,y-(xcap-x)
    if rno==8:
        if x+y>=ycap and x>0:
            x,y=x-(ycap-y),ycap
    if rno==9:
        if x+y<=xcap and y>0:
            x,y=x+y,0
    if rno==10:
        if x+y<=ycap and x>0:
            x,y=0,x+y
    print("X =" ,x)
    print("Y =" ,y)
    if (x==xf and y==yf):
        print(" The result is a Goal state")
        break