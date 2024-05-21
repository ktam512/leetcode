class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # Create a max-heap by inserting negative values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            # Extract the two largest elements (invert back to positive)
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            if first != second:
                # If they are not equal, push the difference back into the heap
                heapq.heappush(max_heap, -(first - second))
        
        # If there's a stone left, return its weight (invert back to positive), else return 0
        return -max_heap[0] if max_heap else 0
        