class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # Create a default dict of lists
        for word in strs:
            anagrams[''.join(sorted(word))].append(word) 
        return list(anagrams.values())


