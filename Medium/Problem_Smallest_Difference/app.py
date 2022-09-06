#############################################################################################################
## Problem: We have to find two closet numbers in two given arrays such that their difference is smallest among 
##          all given numbers
## Explanation: So our strategy is to use two pointer algo. So one pointer will be at the starting position of
##              of 1st array and second pointer be at the starting position of 2nd array. Now we will compute the
##              difference of these two numbers. If the number in the 2nd array is greater than the number in 1st
##              array then we will simply increment 1st array pointer until it is greater. It is because arrays 
##              are sorted so incrementing the array with smaller value will takes us close to the number in the 
##              2nd array. Similarly if 2nd array element is smaller then we will increment 2nd array until it 
##              is greater element in 1st array.
###############################################################################################################

def smallest_diff(array_1,array_2):
    array_1.sort()
    array_2.sort()
    left_pointer = 0
    right_pointer = 0
    diff = 10000
    while left_pointer < len(array_1)  and right_pointer < len(array_2):
        if array_1[left_pointer] < array_2[right_pointer]:
            current_diff = abs(abs(array_1[left_pointer]) - abs(array_2[right_pointer]))
            if current_diff < diff:
                diff = current_diff
                closet_numbers = (array_1[left_pointer],array_2[right_pointer])
            left_pointer +=1
        elif array_1[left_pointer] > array_2[right_pointer]:
            current_diff = abs(abs(array_1[left_pointer]) - abs(array_2[right_pointer]))
            if current_diff < diff:
                diff = current_diff
                closet_numbers = (array_1[left_pointer],array_2[right_pointer])
            right_pointer +=1
    
    return closet_numbers










array_1 = [-1,5,10,20,28,3]
array_2 = [26,134,135,15,17]
a = smallest_diff(array_1,array_2)
print(a)



###########################################################################################################
## Time Complexity: O(nlogn + nlogm) as we are sorting two arrays
## Space Complextiy: O(1) as we are only sending 2 elements.
###########################################################################################################