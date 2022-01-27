"""
Given an array of integer as input, count the single digit numbers in the array. Note that all the numbers in the array are non negative.
Input-> [4,14,6,12,345,5,1]
Output-> Single Digit : 4
"""
ls = [4,14,6,12,345,5,1]
ln = len(ls)
count = 0
for i in range(0,ln):
  e = ls[i]
  if(e>=0) and (e<=9):
    count += 1
print(f"Single Digit: {count}")
