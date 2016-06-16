def anagram2(str1,str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    #check the edge case
    if len(str1)== len(str2):
        print ("anagram possible")
    else:
        print ("anagram is not possible")

    count = {}
    for x in str1:
        if x not in count:
            count[x] = 1
        else:
            count[x] +=1
    print count
    count1 = {}
    for x in str2:
        if x not in count1:
            count1[x] = 1
        else:
            count1[x] +=1
    print count1
    """
    for x in str2:
        if x in count:
            count[x] -= 1
        else:
            return False

    for val in count:
        if count[val] != 0:

            return False
        else:
            return True
    """
    if count == count1:
        return True
    else:
        return False

str1 = ("mother in law")
str2 = ("hitler woman")
if anagram2(str1,str2):
    print ("It is an anagram")
else:
    print ("not anagram")
