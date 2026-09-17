class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        collect = {}

        for num in nums :

            collect[num] = collect.get(num,0) + 1

        sorted_the_dict  = sorted(collect.items(),key = lambda pair: pair[1],reverse=True)

        return [pair[0] for pair in sorted_the_dict[:k]]

