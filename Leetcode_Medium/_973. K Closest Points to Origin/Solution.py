import heapq

class Solution:
    def kClosest(self, points, k):
        minHeap = []
        
        for point in points:
            distance = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(minHeap, (-distance, point))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        result = [point for _, point in minHeap]
        return result