class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m-1
        j = n-1
        k = m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
    
    # If there are any remaining elements in nums2, copy them over
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
