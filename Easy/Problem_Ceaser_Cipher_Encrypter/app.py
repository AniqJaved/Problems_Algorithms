#############################################################################################################
##Problem: So the problem is to get a key from user and then shift alphabets of strings according to that key
#############################################################################################################



def ceaser_cipher(string,key):
    encrypted_list = []
    for alphabet in string:
        ord_code = ord(alphabet)
        if ord_code >96 and ord_code<123:
            asci = ord(alphabet) - 97
            encrypted_char = asci + key
            if(encrypted_char >= 26):
                encrypted_char = encrypted_char % 26
            encrypted_list.append(chr(encrypted_char + 97))
        else:
            encrypted_list.append(alphabet)
    encrypted_string = "".join(encrypted_list)
            
    return encrypted_string
    
    
a = ceaser_cipher("middle-outz",2)
print(a)


#############################################################################################################
## Time Complexity: O(n)
## Space Complexity: O(n)
##############################################################################################################