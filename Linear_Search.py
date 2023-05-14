#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Data Structures~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#                                                                    Linear Algorithm 

def linear_search(list, target): 
    '''
    Returns the index position of a target if found else returns none ( This is Called a Doc String)
    '''
    for i in range(0, len(list)):    #len gathers the TOTAL number of values in a sequence. len Is used here to help range the values from 0 to the 
        if list[i] == target:        #Range generates a sequence of intergers for the values in the list. These values are used as indices.
            return i                 #This alogorithm is considered to have a constant speed of n. 
    return None
    

def veirfy(index):
    if index is not None:
        print("Target found at index: ", index)
    else: 
        print("Target not found in list")


numbers = [1,2,3,4,5,6,7,8,9,10]     #Is the list
result = linear_search(numbers, 4)   #Calls the linear_search function with the inputs of numbers(list made above), and the given target (4). The variable (result) is 
                                     #Given the values of what we processed. 
veirfy(result)  
                                     #the variable result is then sent through the function verify, which checks for any value. If the value that was returned and,
                                     #applied to result is None, the verify will assume the target was not in the sequence.
