sentence = input ("Enter your sentence: ").lower()
freq = {}

for i in sentence:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Result  is :\n " + str(freq))
