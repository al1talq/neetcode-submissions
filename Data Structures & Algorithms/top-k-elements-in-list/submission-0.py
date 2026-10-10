class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequent_counter = Counter(nums)
        most_common = frequent_counter.most_common(k)
        print(most_common)
        
        solutions_list = []
        
        for tpls in most_common:
            i = tpls[0]
            solutions_list.append(i)
        return solutions_list