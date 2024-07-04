class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split_with_max_sum(max_sum):
            count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
                else:
                    current_sum += num
            return True
        
        # Binary search for the minimum possible largest sum
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if can_split_with_max_sum(mid):
                right = mid
            else:
                left = mid + 1
        
        return left