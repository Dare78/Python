#count of number of words and letters
wc ={}
ltr = {}
'''this code list the count of number words and letters in the goven text file'''
with open("test.txt", 'r') as fout:
    output = fout.read().lower()
        #print(output)
    new = output.split()

def wl_count():
    #number of words
    for words in new:
        if words not in wc:
            wc[words]=1
        else:
            wc[words]+=1
    for w in wc:
        print(wc[w],w)

    # number of letter
def l_count():
    for words in new:
        for l in words:
            if l not in ltr:
                ltr[l]= 1
            else:
                ltr[l]+= 1
        for k in ltr:
            print(ltr[k], k)

if __name__=='__main__':
    wl_count()
    l_count()
