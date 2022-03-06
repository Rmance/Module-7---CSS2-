#-------------------------------------------------------------------------------
#Name: Richard Mance
#Date: 3/4/22

#Purpose: With the methods of a function, multiplying all the numbers in a list
#-------------------------------------------------------------------------------

def multi_Pie(myList):
    numby = 1
    for x in myList:
        numby = numby * x

    return numby

Bunny = [5, 2, 7, -1]

print(multi_Pie(Bunny))
