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
        if len(string) % 2 != 0:
            if index != len(string) // 2:
                if index>0:
                    if (palindrome_list.peek() == char.lower()) or (palindrome_list.peek() == char.upper()):
                    
                        palindrome_list.pop()
                    else:
                        palindrome_list.push(char)
                        
                else:
                    palindrome_list.push(char)
                    
        else:
            if index>0:
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

def remove_spaces_special_chars(string):
    palindrome_list = []
    for char in string:
        ord_code = ord(char)
        if (ord_code >96 and ord_code<123) or (ord_code>64 and ord_code < 91):
            palindrome_list.append(char)
    
    palindrome_str = "".join(palindrome_list)
    return palindrome_str




a = palindrome("A man, a plan, a canal: Panamas")
print(a)