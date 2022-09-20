class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = 0
        n2 = 0
        med = []
        while nums1 or nums2:
            if (nums1 and not nums2) :
                med.append(nums1.pop(0))
            elif (not nums1 and nums2):
                med.append(nums2.pop(0))
            elif nums1[0] < nums2[0]:
                med.append(nums1.pop(0))
            elif nums1[0] > nums2[0]:
                med.append(nums2.pop(0))
            elif nums1[n1] == nums2[n2]:
                med.append(nums1.pop(0))
                med.append(nums2.pop(0))
        print(med)
        if len(med)%2==0:
            return (med[(len(med)/2)-1] + med[(len(med)//2)])/2.0
        return med[len(med)/2]
                
                
                