import sys

str1 = raw_input("enter the string 1:")
str2 = raw_input("enter the string 1:")

list1 = list(str1)
list2 = list(str2)

if len(list1)==len(list2):
	print ("lenght match")
else:
	print ("lenght mismatch")
	 
if list1==list2:
	print ("both strings match")
else:
	print("string dont match")
