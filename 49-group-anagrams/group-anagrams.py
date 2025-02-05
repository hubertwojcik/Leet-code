class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hash_table = {}


        for string in strs:
            cardinal = ('.').join(sorted(string))
            if cardinal in hash_table:
                hash_table[cardinal].append(string)
            else:
                hash_table[cardinal] = [string]
        return list(hash_table.values())
            
