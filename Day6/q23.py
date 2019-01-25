# Implement Binary Search
# Algorithm
#     1.Keep track of two pointers First and Last, these are incremented or decremented to limit the part of the list to be searched.
#     2.Find the middle element of the list: mid = ( length of the list )/2
#     3.Compare the middle element with the value to be found
#     4.Check if the middle element is lesser than the value to be found:
#     5.If yes, the element must lie on the second half of the list
#     6.If no, the element must lie on the first half of the list
#     7.Repeat steps 1 through 3 until the element is found or the end of the list is reached.
# Note:The array or list should be shorted.


def binarySearch(ls, data):
   first = 0
   last = len(ls)-1
   done = False
   while first <= last and not done:
       mid = (first+last)//2
       if ls[mid] == data:
           done = True
       else:
           
            if ls[mid]>data:
                last = last-1
            else:
                first = first+1
    return done
print(binarySearch([2,5,7,8,9,11,14,16],4))