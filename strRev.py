def strRev(s):
    lst = []
    count = 1

    for x in s:
        lst.append(s[len(s)-count])
        count += 1

    lst = ' '.join(lst)
    print (lst)

strRev("hello")
