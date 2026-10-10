class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dupe_list = []
        dupe_count = 0
        
        for i in nums:
            if i not in dupe_list:
                dupe_list.append(i)
            else:
                dupe_count += 1
        if dupe_count >= 1:
            return True
        else:
            return False
