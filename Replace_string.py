import re
def replace_string(sout,s1,s2):
    print("Before replacing: %s " %sout)
    new = re.sub(s1,s2,sout)
    print("After replacing : %s" %new)

if __name__=='__main__':
    str = "hi am abc, i live in abc"
    s1 = "abc"
    s2 = "sbp"
    replace_string(str,s1,s2)
