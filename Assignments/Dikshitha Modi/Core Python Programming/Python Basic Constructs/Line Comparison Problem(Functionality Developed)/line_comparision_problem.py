#UC1
print("Welcome to Line Comparison Computation Program") 

import math
x1=int(input("enter value of point x1:"))
x2=int(input("enter value of point x2:"))
y1=int(input("enter value of point y1:"))
y2=int(input("enter value of point y2:"))

#UC2
length1=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("length of line1 is:",length1)

#Line 2 points
x3=int(input("enter value of point x3:"))
x4=int(input("enter value of point x4:"))
y3=int(input("enter value of point y3:"))
y4=int(input("enter value of point y4:"))

length2=math.sqrt((x4-x3)**2+(y4-y3)**2)
print("length of line2 is:",length2)

#UC3
#compare lines
if length1>length2:
    print("Line 1 is greater than Line 2")
elif length1<length2:
    print("Line 1 is less than Line 2")
else:
    print("Both lines are equal")
    

#UC4 - Equity Check
if length1==length2:
    print("Both Lines are equal")
else:
    print("Both Lines are not equal")
