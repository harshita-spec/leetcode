# recursion: when a function calls itself until a specified condition is met.

# print name N times
# TC : O(N).    SC : O(N)
def fun(i,n):
    if i > n:
        return 0
    print("harshita")
    fun(i+1,n)
n=5
fun(1,5)
print()

# Print linearly from 1 to N
def fu(i,n):
    if i > n:
        return 0
    print(i)
    fu(i+1,n)
n=5
fu(1,n)
print()

# Print linearly from N to 1
def fu(i,n):
    if i > n:
        return 0
    fu(i+1,n)
    print(i)
n=5
fu(1,n)
print()

