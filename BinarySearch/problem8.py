# The Peak of a Mountain Array
# Prerequisite: Vanilla Binary Search and Finding the Boundary with Binary Search
#
# A mountain array is defined as an array that
#
# has at least 3 elements has an element with the largest value called "peak", with index k. The array elements
# strictly increase from the first element to A[k], and then strictly decrease from A[k + 1] to the last element of
# the array. Thus creating a "mountain" of numbers. That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1],
# we need to find the index k. Note that the peak element is neither the first nor the lastIndex of the array.
#
# Find the index of the peak element. Assume there is only one peak element.
#
# Input: 0 1 2 3 2 1 0
#
# Output: 3
#
# Explanation: The largest element is 3, and its index is 3.

from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1] or mid == len(arr) - 1:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res


print(peak_of_mountain_array([0,1,2,3,2,1,0]))
print(peak_of_mountain_array([0,10,3,2,1,0]))