##############################################################################################################
## Problem: We are given a string and we have to find out that which first character is non-repeating
## Explanation: So we have created a dictionary in which we are storing the characters and checking the first 
##              character which is not repeating.
###############################################################################################################

from collections import defaultdict
def first_non_repeating(string):
    non_repeating_char_dict = {}
    
    for char in string:
        if char not in non_repeating_char_dict:
            non_repeating_char_dict[char] = 1
        else:
            non_repeating_char_dict[char] += 1
    
    for char in string:
        if non_repeating_char_dict[char]==1:
            return char
    
    return "No first non repeating character found"










a = first_non_repeating("abcdcaf")
print(a)