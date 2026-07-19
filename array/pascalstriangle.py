# 118. Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]

def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)
n=5
r=3
print(nCr(n-1, r-1))
print()

def pascalrow(N):
    row = []
    val = 1
    row.append(val)
    for k in range(1, N):
        val = val * (N - k) // k
        row.append(val) 
    return row
n=3
print(pascalrow(n))
print()

def pascalTriangle(n):
    ans = []
    for row in range(1, n+1):
        tempLst = [] 
        for col in range(1, row+1):
            tempLst.append(nCr(row - 1, col - 1))
        ans.append(tempLst)
    return ans
n = 7
ans = pascalTriangle(n)
for it in ans:
    for ele in it:
        print(ele, end=" ")
    print()

def generate(n):
    ansl=[]
    ans=1 
    ansl.append(ans)
    for i in range(n):
        ans=ans*(n-i)
        ans=ans//(i+1)
        ansl.append(ans)
    return ansl
def pascal(n):
    ans=[]
    for i in range(n):
        ans.append(generate(i+1))
    return ans
n=5
ans = pascal(n)
for it in ans:
    for ele in it:
        print(ele, end=" ")
    print()
