class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for text in strs:
            counter = {}
            for c in text:
                counter[c] = counter.get(c, 0) + 1
            key = tuple(sorted(counter.items()))
            if key in hash_map:
                hash_map[key].append(text)
            else:
                hash_map[key] = [text]
                

        return list(hash_map.values())
        