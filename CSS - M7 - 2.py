#-------------------------------------------------------------------------------
#Name: Richard Mance
#Date: 3/4/22

#Purpose: With the methods of a function, seeing if a given number is in range
#-------------------------------------------------------------------------------

def Range(r):
    if (1 <= r <= 30):
        print("The number is in range")
    else:
        print("The number is not in range")


for i in range(1,10):
    number = int(input("What is the number?: "))
    Range(number)
