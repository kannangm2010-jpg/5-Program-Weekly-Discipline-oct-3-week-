
"""
Sum Square Difference
Problem 6
The sum of the squares of the first ten natural numbers is,
1 ^ 2 + 2 ^ 2 +...+10^ 2 =385.
The square of the sum of the first ten natural numbers is,
(1+2+...+10)2 = 552 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 -3852640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
sus = sum(i**2 for i in range(1, 101) )
k=sum(i for i in range(1, 101))
print(k*k-sus)

