#############################################################################################################
## Problem: We are given a array and we have to find out that which three numbers when summed up leads to a target
##          number given.
## Explanation: So our strategy is to use two pointer algo. So we will be taking one element of array as it is
##              and then the next to that and last element are taken at which we are pointing our pointers.
##              Now whenever the current sum is less then target sum we will move our left_pointer cuz this will
##              increase the total sum (As the array is sorted). Similarly when we have current sum equal to target
##              sum then we move both pointers.
###############################################################################################################





def three_no_sum(array,target_sum):
    sum_array = []
    current_element_pointer = 0
    left_element_pointer = 1
    right_element_pointer = len(array) - 1
    for index,element in enumerate(array):
        current_element = element
        while left_element_pointer < right_element_pointer:
            current_sum = element + array[left_element_pointer] + array[right_element_pointer]
            if current_sum < target_sum:
                left_element_pointer +=1
            elif current_sum > target_sum:
                right_element_pointer -=1
            elif current_sum == target_sum:
                sum_array.append((element, array[left_element_pointer],array[right_element_pointer]))
                left_element_pointer +=1
                right_element_pointer -=1
        index_for_left_pointer = index + 1
        if index_for_left_pointer != len(array):
            left_element_pointer = index_for_left_pointer 
            right_element_pointer = len(array) - 1
    
    return sum_array






array = [12,3,1,2,-6,5,-8,6]
target_sum = 0
array.sort()
a = three_no_sum(array,target_sum)
print(a)


###########################################################################################################
## Time Complexity: O(n2) 
## Space COmplextiy: O(n) as we are expecting whole array to be making triplets leading to target sum.
###########################################################################################################