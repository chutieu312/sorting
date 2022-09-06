
# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index

import random
import time


def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L)):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]

randomlist = random.sample(range(-1000, 1000), 100)
# print(randomlist)
start_time = time.time_ns()
selection_sort(randomlist)
print("It took %s micro seconds ---" % round((time.time_ns() - start_time)/1000))
# print('The array after sorting in Ascending Order by selection sort is:')
# print(randomlist)
