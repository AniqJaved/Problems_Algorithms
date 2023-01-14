#############################################################################################################
## Problem: We have are given with an array [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
## 
##          We have to compute the longest peak. This means that when going leftward or downward we are having
##          a decreasing trend. Even two same points are not allowed
## 
## Explanation: So our strategy is to make an array, which contains all the peaks. Meaning the indexes whose
##              adjacent values are lower than that. Then we will traverse leftward and rightward and will be
##              calculating sum of all the indexes untill the value is of the adajacent index is greater than the 
##              the index itself.
##              So two variables right and left will be summed up to check the length of all the peaks 
###############################################################################################################





def longest_peak(arr):
    len_arr = len(arr)
    peaks_arr = []
    max_peak_length = 0
    i = 0

    # Taking highest point of all the peaks, as per their indexes.

    while i < len_arr-1:
        while i < len_arr-1 and arr[i+1] >= arr[i]:
            i = i + 1
        if i > 0 and i < len_arr-1 and arr[i] > arr[i+1] and arr[i] > arr[i-1]:
            peaks_arr.append(i)
        i+=1

    # Calculating the length of all the peaks by going leftward and rightward on both sides.

    for k in peaks_arr:
        left = 0
        right = 0
        i = k
        j = k
        while i > 0 and i < len_arr-1 and arr[i] > arr[i - 1]:
            left = left + 1
            i = i - 1
        while j > 0 and j < len_arr-1 and arr[j] > arr[j + 1]:
            right = right + 1
            j = j + 1
        
        peak_length = right + left + 1
        if(max_peak_length < peak_length):
            max_peak_length = arr[k]
            
            
arr = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
longest_peak(arr)



###########################################################################################################
## Time Complexity: O(n^2) as we are using nested loops.
## Space Complextiy: O(m) where m is the number of peaks in the array.
###########################################################################################################