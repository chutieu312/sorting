
# Python program for implementation of Bubble Sort
 
 
from lib2to3.pgen2.pgen import DFAState


def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for red in range(n-1,i,-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[red-1] > arr[red]:
                arr[red-1], arr[red] = arr[red], arr[red-1]
 
 
# Driver code to test above
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]
  print(arr)
  bubbleSort(arr)
 
  print("Sorted array is:")
  for i in range(len(arr)):
      print("%d" % arr[i], end=" ")