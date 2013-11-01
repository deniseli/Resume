# Find all the taxicab numbers less than or equal to N
# The nth taxicab number, typically denoted Ta(n) or Taxicab(n), is defined as 
# the smallest number that can be expressed as a sum of two positive algebraic 
# cubes in n distinct ways.

import math

N = (int)(raw_input("Enter an integer N:\n>"))
range_max = (int)(math.ceil(N ** (1/3.0)))  # cube root of N

pairs = []
for i in range(1, range_max):
    for j in range(i, range_max):
        if i ** 3 + j ** 3 <= N:
            pairs.append(i ** 3 + j ** 3)
        else:
            j += 1

pairs.sort()

n = 1
taxicab_numbers = []
for i in range(0, len(pairs)):
    has_n_ways = True
    for j in range (i, i + n):
        if j > len(pairs) - 1 or pairs[j] != pairs[i]:
            has_n_ways = False
    if has_n_ways:
        taxicab_numbers.append(pairs[i])
        i += n - 1
        n += 1

print taxicab_numbers
