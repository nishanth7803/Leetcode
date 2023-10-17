hash_map = {}

for i,n in enumerate(nums):
    diff = target - n
    if diff in hash_map:
        return i,hash_map[diff]
    hash_map[n]=i