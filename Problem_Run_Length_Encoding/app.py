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
