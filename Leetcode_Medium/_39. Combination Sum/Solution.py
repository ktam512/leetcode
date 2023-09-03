class Solution:
    def combinationSum(self, candidates, target):
        self.res = []
        self.candidates = candidates
        self.backtrack([], 0, target)
        return self.res
    
    def backtrack(self, path, indx, target):
        
        if target < 0:
            return
        
        if target == 0:
            self.res.append(path)
            return 
        
        for x in range(indx, len(self.candidates)):
            self.backtrack(path+[self.candidates[x]], x, target - self.candidates[x])