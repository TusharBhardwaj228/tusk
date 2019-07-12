##sum of two numbers
number1,number2=input("enter two numbers: ").split(",")
number1=float(number1)
number2=float(number2)
sum=number1+number2
print("the sum is"  " " + str(sum))

##gst
amt=float(input("enter the amount: "))
gst=amt*18/100
tmt=amt+gst
print(f"the gst is {round(gst,3)}")
print("the total amount is " " " + str(round(tmt,3)))

##area of circle
radius=float(input("enter the radius: "))
area=3.14*radius*radius
print("the area of circle is {}".format(round(area,2)))

##sweaping of 2 values using 3rd variable
a,b=input("enter the two values:").split(",")
a=int(a)
b=int(b)
print(f"before sweaping a= {a}, b={b}")
c=b
b=a
a=c
print(f"after sweaping a= {a}, b={b}")

## sweaping of 2 values without using 3rd variable
a,b=input("enter two numbers: ").split(",")
a=int(a)
b=int(b)
print("before sweaping a={}, b={} ".format(a,b))
a=a+b
b=a-b
a=a-b
print("after sweaping a={}, b={} ".format(a,b))

##odd/even
number=int(input("enter the number: "))
if number%2==0:
    print("even")
else:
    print("odd")

##larger between 2 numbers
a,b=input("enter two numbers: ").split(",")
a=int(a)
b=int(b)
if a>b:
    print(f"greater number is {a}")
else:
    print(f"greater number is {b}")

##grading system
english,maths,science,hindi=input("enter the marks: ").split(",")
english=float(english)
maths=float(maths)
science=float(science)
hindi=float(hindi)
total_marks=english+maths+science+hindi
percentage=(total_marks/400)*100
if total_marks<=400:
    print(f"total marks are {total_marks}")
else:
    print("invalid marks")
if percentage<=100:
    print(f"percentage is {percentage}")
else:
    print("invalid percentage")
if 100>=percentage>=90:
    print("A grade")
elif 90>percentage>=80:
    print("B grade")
elif 80>percentage>=70:
    print("C grade")
else:
    print("fail")