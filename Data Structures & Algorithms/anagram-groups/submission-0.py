class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can use a counter to count the number of times a character appears
        # need to go through the elements one by one
        # Initialize a dictionary to store grouped anagrams
        anagram_groups = {}

        for s in strs:
            # 1. Count character frequencies
            char_counts = Counter(s)
    
            # 2. Convert to a hashable tuple key: (('a', 1), ('c', 1), ('t', 1))
            group_key = tuple(sorted(char_counts.items()))
    
            # 3. Group matching items together 
            if group_key not in anagram_groups:
                anagram_groups[group_key] = []
            
            anagram_groups[group_key].append(s)

        # Print final grouped result
        return (list(anagram_groups.values()))