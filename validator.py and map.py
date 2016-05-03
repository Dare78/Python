#validator
s= "sBp123"
print any(c.isalnum() for c in s)
print any(c.isdigit() for c in s)
print any(c.isalpha() for c in s)
print any(c.islower() for c in s)
print any(c.isupper() for c in s)

#map
print(map(lambda x: x**2, [1,2,3]))

#use of split and join

str = ("hi how are you")
y = str.split(" ")
#after spliting the string
print (y)

z = " ".join(y)
#after joining the string
print ("After joining the string : " + z)
