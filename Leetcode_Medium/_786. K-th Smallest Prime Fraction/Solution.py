class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        l, r = 0.0, 1.0
        
        while l < r:
            m = (l + r) / 2
            max_f = 0.0
            total = 0
            p, q = 0, 0
            j = 1
            
            for i in range(n - 1):
                while j < n and arr[i] > m * arr[j]:
                    j += 1
                if n == j:
                    break
                total += (n - j)
                f = arr[i] / arr[j]
                if f > max_f:
                    max_f = f
                    p, q = i, j
            
            if total == k:
                return [arr[p], arr[q]]
            elif total > k:
                r = m
            else:
                l = m
        
        return []