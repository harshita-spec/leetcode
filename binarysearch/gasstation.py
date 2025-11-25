# Minimize Max Distance to Gas Station

# Given a sorted array arr of size n, containing integer positions of n gas stations on the X-axis, and an integer k, place k new gas stations on the X-axis.
# The new gas stations can be placed anywhere on the non-negative side of the X-axis, including non-integer positions.
# Let dist be the maximum distance between adjacent gas stations after adding the k new gas stations.
# Find the minimum value of dist.
# Your answer will be accepted if it is within 1e-6 of the true value.
# Examples:
# Input: n = 10, arr = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10], k = 9
# Output: 0.50000
# Explanation:
# One of the possible ways to place 10 gas stations is [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10].
# Thus the maximum difference between adjacent gas stations is 0.5.
# Hence, the value of dist is 0.5.
# It can be shown that there is no possible way to add 10 gas stations in such a way that the value of dist is lower than this.

def gasstation(arr, n, k):
    low = 0
    high = 0
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])

    diff = 1e-6
    while high - low > diff:
        mid = (low + high) / 2.0
        count = countofstation(arr, mid)
        if count > k:
            low = mid
        else:
            high = mid
    return high


def countofstation(arr, mid):
    count = 0
    for i in range(1, len(arr)):
        gap = arr[i] - arr[i - 1]
        count += int(gap // mid)
    return count


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
n = len(arr)
k = 9
result = gasstation(arr, n, k)
print(round(result, 6))
