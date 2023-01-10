#############################################################################################################
## Problem: We have are given with an array [5,1,4,2]
## 
##          We have to compute the product of all the array numbers except the one we are having our pointer on.
##          This means that at the 0th index we will be having product of 1x4x2, 1th index 5x4x2 and e.t.c
## 
## Explanation: So our strategy is to make two arrays, left array is giving us the product of all the elements
##              to the left of that particular index. For instance 1th index in left_array will be giving 5,
##              similarly 2nd index of the left_array will be giving 5 x 1, third index will be giving us 
##              5 x 1 x 4. 
##              Similarly we will be calculating the right_array which will be giving us the product to the 
##              right of every element.
##              Note: Here the 0th index of left array and last index of right array is 1 because we are starting
##              the value of product as 1. It is similar to the concept that we started value of sum as 0.
###############################################################################################################





def product_of_array(arr):
    left_array = []
    right_array = []
    product_array = []
    len_of_arr = len(arr)
    product = 1
    
    # Making right array
    for i in range(0,len_of_arr):
        left_array.append(product)
        product = product * arr[i]
    product = 1
    
    # Making left array
    for i in reversed(range(0,len_of_arr)):
        right_array.append(product)
        product = product * arr[i]
    right_array.reverse()
    
    #Making product of array
    
    for i in range(0,len_of_arr):
        product_array.append(left_array[i] * right_array[i])
    
    print(product_array)



arr = [5,1,4,2]
product_of_array(arr)


###########################################################################################################
## Time Complexity: O(n) as we are using no nested loop but we are still using three loops so we have 3n
## Space Complextiy: O(n) as we are putting product corresponding to every element of array. But we are 
##                   still using three arrays so we have 3n.
###########################################################################################################