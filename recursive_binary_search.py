


def recursive_binary_search(list, target):
    if len(list) == 0:                                                     # This line checks to make sure that the list is not empty 
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target) # This return statement and the one below it end up creating entirely new list based off
            else:                                                         # The original one that was sent to be processed, which are sent through the same function
                return recursive_binary_search(list[:midpoint], target)   # recursivly. The whole idea of recurssion is that the algorithm is called with a sequence and,
                                                                          # The aglorithm keeps sending the same sequence through the same algorithm with a return statement
                                                                          # until the target is found or a exception is formed. The number of times a recursive function calls itself is called recursive depth. 
def verify(result):                                                       
    print("Target found: ", result)                                       
                                                                          # : Is used to slice the list, and if you dont have any value on one side of the : it will automatically auto fill to the start or end of the list. 
numbers = [0,1,2,3,4,5,6,7,8]                                             #
result = recursive_binary_search(numbers, 12)                             # Some langauges are better then others for recursion. Python for example may give a
verify(result)                                                            # maximum "recursion depth exceeded" error if the recursive function calls istelf too many times.
                                                                          
result = recursive_binary_search(numbers, 6)
verify(result)
