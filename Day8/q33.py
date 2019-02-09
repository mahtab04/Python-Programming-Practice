# Implementation of bubble sort
def bubble_Sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]


arr = [64, 34, 25, 12, 22, 11, 90]
 
bubble_Sort(arr)
for i in range(len(arr)):
    print(arr[i])