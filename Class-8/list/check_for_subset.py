def check_for_subset(set1:set, set2:set):
    return set2.issubset(set1)

res = check_for_subset({1, 2, 3, 4, 5}, {2, 3, 4})
print(res)