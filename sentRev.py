def sentRev(s):
    words = []
    spaces = [' ']
    length = len(s)
    i = 0
    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1

    print (" ".join(reversed(words)))

sentRev("hi how are you")
