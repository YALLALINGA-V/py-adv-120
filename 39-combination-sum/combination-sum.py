class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        candidates.sort()
        
        def backtrack(remain: int, combo: list[int], start: int):
            if remain == 0:
                results.append(list(combo))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                combo.append(candidates[i])
                backtrack(remain - candidates[i], combo, i)
                combo.pop()
                
        backtrack(target, [], 0)
        return results



    