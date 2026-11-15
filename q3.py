a=int(input("enter time in hours"))
if a>=0:
    b=a*60
    c=a*3600
    print("time in minutes is",b)
    print("time in seconds is",c)
else:
    print("error invalid time")
