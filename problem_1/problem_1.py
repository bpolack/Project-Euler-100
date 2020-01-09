# Solution to Project Euler Problem 1

#### Problem: 
#### If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#### Find the sum of all the multiples of 3 or 5 below 1000.

multiples = set()
def get_multiples(x, max_multiple):
    i = 1
    while (True):
        multiple = x * i
        if (multiple < max_multiple):
            multiples.add(multiple)
            i += 1
        else:
            break

# Get multiples of 3 and 5 below 1000
get_multiples(3, 1000)
get_multiples(5, 1000)

# Sum of all multiples in set
total = sum(multiples)

print( "Sum of all multiples of 3 or 5 below 1000 : " + str(total) )