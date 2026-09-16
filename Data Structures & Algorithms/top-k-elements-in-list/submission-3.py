class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collect = {}

        for num in nums:
            collect[num] = collect.get(num,0)+1 
        
        result = sorted(collect.items(), key = lambda pair : pair[1],reverse=True)

        answer = []

        for pair in result[:k]:
            answer.append(pair[0]);
        return answer
        
        
