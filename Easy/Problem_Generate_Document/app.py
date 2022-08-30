########################################################################################################################
## Problem: In this problem we are given two strings one is characters and other is document. What we have to do is
##          that we have to check that if the characters string can make a string in the document.
## Strategy: So our strategy is to make two dictionaries containing count of each character in both the strings. Now 
##           we will check that if the count of each character in the document string is less than or equal to the
##           count of same characters in the characters string. It means that even if the characters string has
##           occuring of "a" 3 and document string has occuring of "a" 2, then we will be able to make the document
##           from given array.
######################################################################################################################


from collections import defaultdict
def generate_doc(characters,document):
    characters_dict = defaultdict(int)
    document_dict = defaultdict(int)
    
    for char in characters:
        if char not in characters_dict:
            characters_dict[char] = 1
        else:
            characters_dict[char] += 1
    
    for doc_char in document:
        if doc_char not in document_dict:
            document_dict[doc_char] = 1
        else:
            document_dict[doc_char] += 1
    
    for char in document_dict.keys():
        if document_dict[char] > characters_dict[char]:
            return False
    
    return True








characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
a = generate_doc(characters,document)
print(a)



#####################################################################################################################
##Time Complexity: O(m+n) as m is number of characters in characters string and n is number of characters in document.
##Space Complexity: O(m+n) as m is number of characters in characters string and n is number of characters in document.
#####################################################################################################################