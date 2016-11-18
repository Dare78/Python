def PigLatin(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    count = 1

    new = s.lower().split()
    print(new)
    for word in new:
        if word[0] not in vowels:
            #case 1: remove first letter and add "ma"
            word = word[1:]
            new_word = word + "ma"

        else:
            # case 2: if word begins with vowel
            new_word = word + "ma"

            #case 3: increment and append j after each word
        string_to_append = "j"*count
        word = "%s%s" %(new_word,string_to_append)
        count+=1
        output.append(word)
    print(" ".join(output))


if __name__ == "__main__":
    s ="I am a pig latin"
    PigLatin(s)

