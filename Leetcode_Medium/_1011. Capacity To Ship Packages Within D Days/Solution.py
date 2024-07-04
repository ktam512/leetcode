class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship_within_capacity(capacity):
            days_needed = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = weight
                else:
                    current_weight += weight
            return days_needed <= days
        
        # Binary search for the minimum capacity
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            if can_ship_within_capacity(mid):
                right = mid
            else:
                left = mid + 1
        
        return left