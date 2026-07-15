# Trapping Rainwater

# Given an array of non-negative integers, height representing the elevation of ground. Calculate the amount of water that can be trapped after rain.
# Example 1
# Input: height= [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
# Explanation: As seen from the diagram 1+1+2+1+1=6 unit of water can be trapped

# Example 2
# Input: height= [4, 2, 0, 3, 2, 5]
# Output: 9
# Explanation: 2+4+1+2=9 unit of water can be trapped

def rainwater(height):
    l=0
    r=len(height)-1
    lmax=rmax=total=0
    while l<r:
        if height[l]<height[r]:
            if height[l]>=lmax:
                lmax=height[l]
            else:
                total+=lmax-height[l]
            l+=1
        else:
            if height[r]>=rmax:
                rmax=height[r]
            else:
                total+=rmax-height[r]
            r-=1
    return total
height= [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rainwater(height))
