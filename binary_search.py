
def binary_search(list, target):
    first = 0                              
    last = len(list) - 1                # In this line of code and the former we are defining indicies. The index will start at 0 and end at the value equal to the
                                        # length of the list - 1. We do - 1 because the index starts at value 0 and python starts the count from 1 when getting the len. 
    while first <= last:
        midpoint = (first + last)//2    # The operator  //  divides and if it does not return a whole number it will round it down to the nearest integer. 
                                        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:      #The changing of the values of the variables *first* and *last* ensures that the loop closes eventually.
            first = midpoint + 1           #This is due to the loop including operators that change the value of local variables being used for the loop.
        else:                              #The main way this algorithm works is by determing if the value of the target is == > or < the middlepoint(first + last)
            last = midpoint - 1            #then by changing the value of the local variables first & last based off if the target is greater then or above the middle point. 
                                           #value of the variables dictating where the mid point goes.
    return None

def veirfy(index):
    if index is not None:
        print("Target found at index: ", index)
    else: 
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]     
result = binary_search(numbers, 4)   
                                     
veirfy(result)  
                                     