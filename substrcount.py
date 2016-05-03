string, substring = [raw_input() for _ in range(2)]
score = 0
for i in range(len(string)):
   if string[i:i+len(substring)] == substring:
        score += 1
print score
