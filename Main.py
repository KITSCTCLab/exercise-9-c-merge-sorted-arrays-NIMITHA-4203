from typing import List

def merge_sort(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  x = nums1[0:m+1]
  y = nums2[0:n+1]
  nums1 = x + y
  
  if len(nums1) > 1:
        mid = len(nums1) // 2
        left = nums1[:mid]
        right = nums1[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              nums1[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                nums1[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            nums1[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums1[k]=right[j]
            j += 1
            k += 1

# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge_sort(nums1, m, nums2, n)
print(nums1)
