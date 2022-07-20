class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j =0 ,len(nums)-1
        while i <j:
            s = nums[i] +nums[j]
            if s> target: j-=1
            if s< target: i+=1
            if s== target: return [nums[i], nums[j]]
        return []
