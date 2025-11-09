# Majority Element-II

# Given an integer array nums of size n. Return all elements which appear more than n/3 times in the array. The output can be returned in any order.
# Examples:
# Input: nums = [1, 2, 1, 1, 3, 2]
# Output: [1]
# Explanation: Here, n / 3 = 6 / 3 = 2.
# Therefore the elements appearing 3 or more times is : [1]
# Input: nums = [1, 2, 1, 1, 3, 2, 2]
# Output: [1, 2]
# Explanation: Here, n / 3 = 7 / 3 = 2.
# Therefore the elements appearing 3 or more times is : [1, 2]

def majorityElement(v):
    n = len(v)
    cnt1, cnt2 = 0, 0 
    el1, el2 = float('-inf'), float('-inf') 
    for i in range(n):
        if cnt1 == 0 and el2 != v[i]:
            cnt1 = 1
            el1 = v[i]
        elif cnt2 == 0 and el1 != v[i]:
            cnt2 = 1
            el2 = v[i]
        elif v[i] == el1:
            cnt1 += 1
        elif v[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ls = [] 
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if v[i] == el1:
            cnt1 += 1
        if v[i] == el2:
            cnt2 += 1

    mini = int(n / 3) + 1
    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)
    return ls

arr = [11, 33, 33,12,11,10,10,21,10,10,10,10, 10,10,11, 33, 11]
ans = majorityElement(arr)
print("The majority elements are: ", end="")
for it in ans:
    print(it, end=" ")
print()
