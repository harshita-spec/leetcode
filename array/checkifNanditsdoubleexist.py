# 1346. Check If N and Its Double Exist

# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 
# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
# Example 2:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

def doubleexist(arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i!=j and (2 * arr[j]) == arr[i]:
                    return True
        return False
arr=[10,2,5,3]
print(doubleexist(arr))

def doublexist(arr):
        st=[]
        for i in range(len(arr)):
            if (2 * arr[i]) in st or (arr[i]/2) in st:
                return True
            st.append(arr[i])
        return False  
arr=[3,1,7,11]
print(doublexist(arr))