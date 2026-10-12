class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0 

        numbers = sorted(nums)
        max_length = 1
        length = 1

        for i  in range(1,len(numbers)):
           
            if numbers[i] == numbers[i-1]:
                continue
            elif numbers[i] == numbers[i-1]+1:
                length +=1
            else:
                 length = 1 

            max_length = max(max_length,length)
            
        return max_length


            

