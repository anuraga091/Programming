#Triangle Quest 2
"""
You are given a positive integer .
Your task is to print a palindromic triangle of size .
1
121
12321
1234321
123454321

"""

#Solution
for i in range(1, int(input())+1):
    print(((10**i - 1)//9)**2)
    