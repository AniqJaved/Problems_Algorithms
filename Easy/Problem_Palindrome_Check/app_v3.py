class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return not self.items
    def __str__(self):
        return str(self.items)

def palindrome(string):
    string = remove_spaces_special_chars(string)
    palindrome_list = Stack()
    for index,char in enumerate(string):
        #For string with odd number of characters. As we will not be considering the middle character cuz it doesnot matter , it will be present at all times.
        if len(string) % 2 != 0:
            #Not considering middle character
            if index != len(string) // 2:
                #Only using this if statement we are having something in the list as we are using peek method and if list is empty it will be giving us an error.
                if index>0 and palindrome_list.is_empty() == False:
                    #Checking that if the character we are peeking and the character which is at the loop both are same regardless of their capitalization
                    if (palindrome_list.peek() == char.lower()) or (palindrome_list.peek() == char.upper()):
                        palindrome_list.pop()
                    else:
                        palindrome_list.push(char)
                else:
                    palindrome_list.push(char)
        #For string with even number of characters      
        else:
            if index>0 and palindrome_list.is_empty() == False:
                if (palindrome_list.peek() == char.lower()) or (palindrome_list.peek() == char.upper()):
                    
                    palindrome_list.pop()
                else:
                    palindrome_list.push(char)
                    
            else:
                palindrome_list.push(char)
                
            
    if palindrome_list.is_empty():
        return True
    else:
        return False

#Function for making string only conatining alphanumeric characters.
def remove_spaces_special_chars(string):
    palindrome_list = []
    for char in string:
        ord_code = ord(char)
        if (ord_code >96 and ord_code<123) or (ord_code>64 and ord_code < 91) or (ord_code > 47 and ord_code < 58):
            palindrome_list.append(char)
    
    palindrome_str = "".join(palindrome_list)
    print(palindrome_str)
    return palindrome_str




a = palindrome(",'6``c4i,::,i4ckk6',")
print(a)