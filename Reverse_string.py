def SentRev(s):
   st = ""
   new = []
   for each in s:
       if each is not " ":
           st = st + each
       else:
           new.append(st)
           st = ""
   new.append(st)
   print(new)

   x = len(new)-1
   reverse =[]
   for i in range(x,-1,-1):
       reverse.append(new[i])
   print(" ".join(reverse))

if __name__=='__main__':
    a = "Linkedin is hiring"
    SentRev(a)





