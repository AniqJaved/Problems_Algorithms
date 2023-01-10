#############################################################################################################
## Problem: We have are given with an array [5,1,4,2]
## 
##          We have to compute the product of all the array numbers except the one we are having our pointer on.
##          This means that at the 0th index we will be having product of 1x4x2, 1th index 5x4x2 and e.t.c
## 
## Explanation: So our strategy is to use two loops and just check that when the pointer of both the loops are same
##              then skip that value.
###############################################################################################################





def product_of_array(arr):
    product = 1
    new_array = []
    len_of_arr = len(arr)
    for i in range(0,len_of_arr):
        product = 1
        for j in range(0,len_of_arr):
            if(i != j):
                product = product * arr[j]
        new_array.append(product)
    
    print(new_array)




arr = [5,1,4,2]
product_of_array(arr)


###########################################################################################################
## Time Complexity: O(n^2) as we are using two loops
## Space Complextiy: O(n) as we are putting product corresponding to every element of array. 
###########################################################################################################