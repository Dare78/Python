#print(map(lambda x: x**2, [1,2,3]))

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2 != 0, fibonacci))
print (odd_numbers)
# explicitly mention x % 2== 0 to return even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print (even_numbers)
