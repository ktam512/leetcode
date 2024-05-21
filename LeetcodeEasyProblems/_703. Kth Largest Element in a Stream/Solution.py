class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.minHeap = []

        # Add each number in nums to the heap
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.minHeap, val)  # Add the new value to the heap
        if len(self.minHeap) > self.k:  # If heap size exceeds k
            heapq.heappop(self.minHeap)  # Remove the smallest element
        return self.minHeap[0]  # The smallest element in the heap is the kth largest
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)