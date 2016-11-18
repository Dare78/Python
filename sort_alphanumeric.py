def sort_items(s):
    out =[]
    new1 =[]
    new = list(s)
    for each in new:
        out.append(ord(each))
        out.sort()
#    print (out)
    for x in out:
        new1.append(chr(x))
    print("".join(new1))
if __name__=='__main__':
    s ="AaBb123"
    sort_items(s)
