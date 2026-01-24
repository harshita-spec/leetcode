# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

def maxArea( height):
        left=0
        right=len(height)-1
        maxi=0
        while left<=right:
            diff=right-left
            if height[left]<=height[right]:
                capacity=height[left]*diff
                if capacity>maxi:
                    maxi=capacity
                left+=1
            else:
                capacity=height[right]*diff
                if capacity>maxi:
                    maxi=capacity
                right-=1
        return maxi
height=[1,8,6,2,5,4,8,3,7]
result=maxArea(height)
print(result)