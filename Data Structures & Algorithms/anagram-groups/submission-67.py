class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) # mapping charCount to List of Anagrams

        for string in strs:
            count = [0] * 26 # a ... z

            for char in string:
                count[ord(char) - ord("a")] += 1 # occurance of each char a-z

            result[tuple(count)].append(string)

        return list(result.values())