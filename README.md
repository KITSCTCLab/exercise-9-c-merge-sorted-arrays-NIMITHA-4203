# Problem Statement

You are given two integer arrays <i>nums1</i> and <i>nums2</i>, sorted in ascending order, and two integers m and n, representing the number of elements to be merged in nums1 and nums2 respectively.</br>

Merge <i>nums1</i> and <i>nums2</i> into a single array sorted in ascending order.</br>

The final sorted array should not be returned by the function, but instead be stored inside the array, <i>nums1</i>. </br>
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements should be ignored. </br>



## Example
```
Input: nums1 = [1,2,3,4,5,6], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

# Constraints
nums1.length == m + n</br>
nums2.length >= n</br>
0 <= m, n <= 200</br>
1 <= m + n <= 200</br>
-10<sup>9</sup> <= nums1[i], nums2[j] <= 10<sup>9</sup>

## Sample Input - 1
```
1, 2, 3, 4, 5, 6
7, 8, 9
4
2
```
First line represents <i>nums1</i>.</br>
Second line represents <i>nums2</i>.</br>
Third line shows m, which represents first four elements from <i>nums1</i> will be processed.</br>
Fourth line shows n, which represents first two elements from <i>nums2</i> will be processed.</br>

## Sample Output - 1
```
[1, 2, 3, 4, 7, 8]
```
## Sample Input - 2
```
7, 8, 9, 10, 11, 12
1, 2, 3, 4
4
2
```
## Sample Output - 2
```
[1, 2, 7, 8, 9, 10]
```
