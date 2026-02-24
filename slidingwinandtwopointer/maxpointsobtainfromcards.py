# Maximum Points You Can Obtain from Cards

# Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. The score is the sum of the scores of the chosen cards.

# Return the maximum score that can be obtained.
# Example 1
# Input : cardScore = [1, 2, 3, 4, 5, 6] , k = 3
# Output : 15
# Explanation : Choosing the rightmost cards will maximize your total score. So optimal cards chosen are the rightmost three cards 4 , 5 , 6.
# Th score is 4 + 5 + 6 => 15.
# Example 2
# Input : cardScore = [5, 4, 1, 8, 7, 1, 3 ] , k = 3
# Output : 12
# Explanation : In first step we will choose card from beginning with score of 5.
# In second step we will choose the card from beginning again with score of 4.
# In third step we will choose the card from end with score of 3.
# The total score is 5 + 4 + 3 => 12

def maxScore(cp, k):
    lsum=0
    rsum=0
    maxsum=0
    for i in range(k):
        lsum=lsum+cp[i]
    maxsum=lsum
    rind=len(cp)-1
    for i in range(k-1,-1,-1):
        lsum=lsum-cp[i]
        rsum=rsum+cp[rind]
        maxsum=max(maxsum,lsum+rsum)
        rind=rind-1
    return maxsum
cardScore=[5, 4, 1, 8, 7, 1, 6 ]
k=3
result=maxScore(cardScore,k)
print(result)
