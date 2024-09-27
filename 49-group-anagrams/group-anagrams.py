class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map={}

        for index,value in enumerate(strs):
            keys = tuple(sorted(value))            
            if keys in hash_map:                
                hash_map[keys].append(value)
            else:
                hash_map[keys]=[value]
        return list(hash_map.values())

        