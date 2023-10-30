# For systematically calculating a Uniformed Distribution of marketing leads such that human bias is removed.

import numpy as np
from numpy import random
from collections import Counter
import statistics


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Uniform Distribution')

# Calculate the distribution of 4 partners (A-D).
# p= odds in example 1 lead / 4 partners = 25% chance of getting a lead
# size= 4 partners, 100 leads to be distributed. Change partner size and total leads to be distributed per partner.
# in example size=(4, 100) = 400 leads to be distributed
x = random.choice(['A', 'B', 'C', 'D'], p=[0.25, 0.25, 0.25, 0.25], size=(4, 100))
print(x)

# Count occurrence of element 'A' in numpy array
count_arr = np.count_nonzero(x == 'A')
print('Total occurrences of "A" in array: ', count_arr)
A = count_arr

# Count occurrence of element 'B' in numpy array
count_arr = np.count_nonzero(x == 'B')
print('Total occurrences of "B" in array: ', count_arr)
B = count_arr

# Count occurrence of element 'C' in numpy array
count_arr = np.count_nonzero(x == 'C')
print('Total occurrences of "C" in array: ', count_arr)
C = count_arr

# Count occurrence of element 'D' in numpy array
count_arr = np.count_nonzero(x == 'D')
print('Total occurrences of "D" in array: ', count_arr)
D = count_arr

# calculate the mean
a = np.array([A, B, C, D])
print('mean: ', np.mean(a))

# calculate the standard deviation from the mean
print('std. deviation', np.std(a))

# comparison to using the statistic library.
print('===========================')
print("statistics lib: Standard Deviation of the sample is % s "% (statistics.stdev(a)))
print("Mean of the sample is % s " % (statistics.mean(a)))
print('===========================')
