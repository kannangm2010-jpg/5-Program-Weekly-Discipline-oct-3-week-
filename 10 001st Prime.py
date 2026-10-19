"""
10 001st Prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001 st prime number?
"""

count = 1
i = 3

while count < 10001:
    
    for j in range(3, int(i**0.5) + 1, 2):
        if i % j == 0:
            break  
    else:
        count += 1
    
    i += 2  

print(i - 2)