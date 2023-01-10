#############################################################################################################
## Problem: We are given a array and we have to remove pattern when we have adjacent A and B or adjacent C and
##          D.
##          
## Explanation: So our strategy is to use two pointer algo. First pointer at the first index and second pointer
##              at the second index. We will compare both the pointer. If the pattern is found we will remove it.
###############################################################################################################

def solution(S):
    string_list = []
    string_list[:0] = S
    ptr1 = 0
    ptr2 = 1
    while ptr2 < len(string_list):
        if(string_list[ptr1] == 'A' and string_list[ptr2] == 'B' or string_list[ptr1] == 'B' and string_list[ptr2] == 'A'):
            string_list = string_list[:ptr1] + string_list[ptr2+1 :]
            ptr1 = ptr1 - 1
            ptr2 = ptr2 - 1
            print(string_list)
        elif(string_list[ptr1] == 'C' and string_list[ptr2] == 'D' or string_list[ptr1] == 'D' and string_list[ptr2] == 'C'):
            string_list = string_list[:ptr1] + string_list[ptr2+1 :]
            ptr1 = ptr1 - 1
            ptr2 = ptr2 - 1
            print(string_list)
        else:
            ptr1 += 1
            ptr2 += 1
            print(string_list, ptr1,ptr2)
    
    properString = ''.join(string_list)
    return properString
        




S = "ACBDACBD"
string = solution(S)

print(string)