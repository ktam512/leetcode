class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def can_cut_ribbons(ribbons, n, L):
            total_pieces = 0
            for ribbon in ribbons:
                total_pieces += ribbon // L
            return total_pieces >= n
        
        def max_ribbon_length(ribbons, n):
            left = 1
            right = max(ribbons)
            result = 0
            
            while left <= right:
                mid = (left + right) // 2
                if can_cut_ribbons(ribbons, n, mid):
                    result = mid  # If we can cut into n pieces of length mid, store this as potential answer
                    left = mid + 1  # Try for a longer length
                else:
                    right = mid - 1  # Try for a shorter length
            
            return result
        
        return max_ribbon_length(ribbons, k)