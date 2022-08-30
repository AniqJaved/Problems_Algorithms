########################################################################################################
##Problem: In this problem we are given a string which follows multiple alphabets. Now we have to decide
##         how many times a alphabet occurs in multiples of 9. It means if goes higher than 9 then we will
##         make separate for alphabets after that "AAAAAAAAAAA" = 9A2A
##Explanation: So the strategy is to first place them in dictionary to get total amount of each alphabet
##             then get the divisor meaning how many 9 that particular alphabet has use divison and to get
##             remaining alphabbets after we have counted 9 of them use modulus.
#########################################################################################################


def parse(string):
    string_dict = {}
    for alphabet in string:
        if alphabet in string_dict:
            string_dict[alphabet] += 1
        else:
            string_dict[alphabet] = 1
    keys = string_dict.keys()
    for key in keys:
        value = string_dict[key]
        
        divisor = value // 9
        reminder = value % 9
        
        if(divisor!=0):
            for i in range(1,divisor+1):
                print(f"9{key}",end="")
        if(reminder!=0):
            print(f"{reminder}{key}",end="")
    



a = parse("AAAAAAAAAAAAABBCCCC")

#########################################################################################################
##Time complexity: O(n^2)
#########################################################################################################