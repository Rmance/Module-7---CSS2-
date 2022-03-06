#-------------------------------------------------------------------------------
#Name: Richard Mance
#Date: 3/4/22

#Purpose: With the methods of a function, taking an old list and making it unique
#Also, sorting it for an addition purpose
#-------------------------------------------------------------------------------

def duplicate(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

Oldlist = [1, 3, 3, 3, 6, 2, 3, 5]
print("Old list: ", Oldlist)

Newlist = duplicate(Oldlist)
Newlist.sort()
print("New list", Newlist)
