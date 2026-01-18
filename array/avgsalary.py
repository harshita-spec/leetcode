# 1491. Average Salary Excluding the Minimum and Maximum Salary

# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

# Example 2:
# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

def average( salary):
    minsal=float('INF')
    maxsal=0
    totalsal=0
    n=len(salary)
    for i in range(n):
        totalsal += salary[i]
        if salary[i] > maxsal :
        	maxsal=salary[i]
        if salary[i] < minsal: 
        	minsal=salary[i]
    totalsum = totalsal - maxsal -minsal
    return  totalsum /(n-2)
salary=[4000,3000,1000,2000]
print(average(salary))