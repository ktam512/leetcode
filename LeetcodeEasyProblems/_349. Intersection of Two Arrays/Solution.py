class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Sort the input arrays to make finding the intersection easier
        nums1.sort()
        nums2.sort()
        
        # Initialize an empty list to store the intersection
        intersection = []
        
        # Initialize pointers for both arrays
        ptr1 = ptr2 = 0
        
        # Iterate through both arrays
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            # If the elements at the current pointers are equal, add one of them to the intersection list
            if nums1[ptr1] == nums2[ptr2]:
                # Avoid duplicates by checking if the current element is already in the intersection list
                if not intersection or nums1[ptr1] != intersection[-1]:
                    intersection.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            # If the element in nums1 is smaller, move ptr1 to the right
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            # If the element in nums2 is smaller, move ptr2 to the right
            else:
                ptr2 += 1
        
        return intersection