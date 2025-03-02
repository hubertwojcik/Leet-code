class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hash_map = {}

        for string in strs:
            letters = [0] * 26
            for char in string:
                char_value = ord(char) - ord('a')
                letters[char_value] += 1
            key = tuple(letters)
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(string)
        return list(hash_map.values())
            
