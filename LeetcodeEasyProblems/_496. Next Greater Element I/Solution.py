class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {} # Store mapping of elements to their next greater element
        stack = [] # Store indices of elements
        
        # Iterate through nums2 to find the next greater element for each element
        for num in nums2:
            while stack and stack[-1] < num:
                mapping[stack.pop()] = num
            stack.append(num)
        
        # Iterate through nums1 to retrieve next greater elements
        for i in range(len(nums1)):
            nums1[i] = mapping.get(nums1[i], -1) # If no next greater element found, store -1
        
        return nums1
