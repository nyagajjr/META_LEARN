def isPalindrome(str):
    startIndex = str[0]
    endIndex = str[-1]
   
    for char in str:
        if startIndex != endIndex:
            return False
    return True

print(isPalindrome('racecar'))

    
    # OR
    # startIndex = 0
    # endIndex = len(str) - 1
    
    # for x in str:
    #     if str[startIndex] != str[endIndex]:
    #         return False
    # return True