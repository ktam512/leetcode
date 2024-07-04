
class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        left, right = 0, len(self.prefix_sums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()