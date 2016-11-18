import re
def freqW():
    count ={}
    alist =[]
    f = open("test.txt",'r')
#    out = f.read().split()
#    print(out)
    matched = re.findall(r'[a-zA-z]+', f.read().lower())
    print (matched)

    for i in matched:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1

    max_val = 0
    max_count = ''
    for k in count:
        if count[k]== max(count[k],max_val):
            max_val = count[k]
            max_count = k
    print(max_count,max_val)

#    import operator
#    new_dict = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
#    print new_dict[0]


if __name__=='__main__':
#    import re
    freqW()
