########################################################################################################
##Problem: In this problem we are given a string which follows multiple alphabets. Now we have to decide
##         how many times a alphabet occurs in multiples of 9. It means if goes higher than 9 then we will
##         make separate for alphabets after that "AAAAAAAAAAA" = 9A2A
##Explanation: The Approach to to check that wether that we iterate over same alphabets but when we
##             encounter new alphabet we append the previous character w.r.t to the number of its 
##             occurences.
#########################################################################################################




def parse(string):
    currentLength = 0
    newString = []
    for index in range(1,len(string)):
        currentLength +=1
        currentPosChar = string[index]
        previousPosChar = string[index-1]
        if currentPosChar != previousPosChar or currentLength == 9:
            newString.append(previousPosChar)
            newString.append(str(currentLength))
            currentLength = 0
        #Taking care of last alphabet which will be ending with currentPosChar equal to previousPosChar
        if index == len(string) - 1:
            newString.append(currentPosChar)
            newString.append(str(currentLength))
    newString = "".join(newString)
    return newString



a = parse("AAAAAAAAAAAAABBCCCC")
print(a)

#########################################################################################################
##Time complexity: O(n)
#########################################################################################################