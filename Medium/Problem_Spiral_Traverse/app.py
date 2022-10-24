#############################################################################################################
## Problem: We have are given a matrix of nummber
##                    1, 2, 3, 4
##                    12,13,14,5
##                    11,16,15,6
##                    10,9, 8, 7
##          Now you can see that we have to move one time horizontally then vertically on the right side
##          then reverse at the bottom and then reverse at the left side. This will give us number in form
##          1,2,3,4,5,6,7,8,9....
## Explanation: So our strategy is to use four pointer algo. One pointer will be representing the starting col
##              second will be representing the starting row, third will be representing the ending col and fourth
##              will be representing the ending row. Now by using these pointers we will be traversing the whole
##              spiral 2D lists. Once the outer shell is completed (in this case we have 1,2,3,4,5...12) we
##              will be moving to inner shell (in this case is 13,14,15,16)
###############################################################################################################




def spiral_traverse(spiral_list):
    start_row = 0
    start_col = 0
    end_row = len(spiral_list) - 1
    end_col = len(spiral_list[0]) - 1
    new_list = []
    
    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col,end_col + 1):        
            new_list.append(spiral_list[start_row][col])
        for row in range(start_row+1,end_row+1):       #We are using +1 with start_row so we can avoid the repetation of the same element in list.
            new_list.append(spiral_list[row][end_col])
        for col in reversed(range(start_col,end_col )):  #We are not using +1 with end_col so we can avoid the repetation of the same element in list.
            new_list.append(spiral_list[end_row][col])
        for row in reversed(range(start_row+1,end_row)): #We are not using +1 with end_row so we can avoid the repetation of the same element in list.
            new_list.append(spiral_list[row][start_col])
        
        
        start_row +=1
        start_col +=1
        end_col -= 1
        end_row -= 1
    print(new_list)







spiral_list = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
spiral_traverse(spiral_list)

########################################################################################################
## Time Complexity: O(n) as we are moving across all the elements one time.
## Space Complextiy: O(n) as we are storing all the elements in one list.
###########################################################################################################