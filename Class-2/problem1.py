s = input("Enter a String: ")

s = list(s.lower())

vowels = ['a', 'e', 'i', 'o', 'u']

vowels_cnt = 0
consonant_cnt = 0

for i in range(0, len(s)):
    if s[i].isalpha() and (not s[i].isspace()):
        if s[i] in vowels:
            vowels_cnt += 1
        else:
            consonant_cnt += 1

print("Vowel: {}, Consonant: {}".format(vowels_cnt, consonant_cnt))