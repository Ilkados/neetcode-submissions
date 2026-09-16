class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for word in strs:
            
            count = [0] * 26 
            for character in word:
                pos = ord(character) - ord("a")
                count[pos]+=1
            
            key = tuple(count)

            if key not in  groups.keys():
                groups[key] = []

            groups[key].append(word)
        
        return [*groups.values()]


                