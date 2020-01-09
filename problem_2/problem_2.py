# Solution to Project Euler Problem 2

#### Problem: 
#### By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Calculate even Fibonacci numbers only
def even_fibs(limit):
    a, b = 0, 2
    total = 0
    while (b <= limit):
        total += b
        a, b = b, 4 * b + a  # Evens only Fibonacci sequence Fn = 4*Fn-1 + Fn-2
    return total

print( "Sum of Even Fibonacci Numbers below 4M : " + str( even_fibs(4000000) ) )