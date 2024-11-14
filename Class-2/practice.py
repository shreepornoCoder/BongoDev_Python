# how count() function is working

def count_word(sentence, word):
    cnt = 0
    for i in sentence:
        if i == word:
            cnt += 1

    return [word, cnt]

s = input()
s = s.split()

res = {}

for char in s:
    val = count_word(s, char)
    word = val[0]
    word_cnt = val[1]
    
    res[word] = word_cnt

print(res) 