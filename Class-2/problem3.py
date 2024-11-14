s = input("Enter a sentence: ")
s = s.split()

# way-1
longest_word = ''

for word in s:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)

# way-2
def longest_word(sentence):
    val = sorted(sentence, key=len)
    print(val[-1])

longest_word(s) 