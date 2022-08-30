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
    palindrome_list = Stack()
    for index,char in enumerate(string):
        if index>0 and palindrome_list.peek() == char:
            palindrome_list.pop()
        else:
            palindrome_list.push(char)
    if palindrome_list.is_empty():
        return True
    else:
        return False





a = palindrome("abccba")
print(a)