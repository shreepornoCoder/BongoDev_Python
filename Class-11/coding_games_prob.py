s = input()
res = ''
odd_nums = []


for c in s:
    if c.isdigit():  
        if int(c) % 2 == 0:  
            val = ord(c) + 17
            res += chr(val)
        else:  
            res += c
            odd_nums.append(c)
    else:  
        res += c

odd_nums.sort(reverse=True)


final_res = ''
digit_index = 0

for i in res:
    if i.isdigit():
        final_res += odd_nums[digit_index]
        digit_index += 1
    else:
        final_res += i

# Output results

print(final_res)
