from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  # Write code here


# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
