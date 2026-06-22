class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)
        result = []

        for string in strs:
            sorted_string = ''.join(sorted(string)) # act, cat: act
            anagrams[sorted_string].append(string)

        # act: [act, cat]
        # aht: [hat]
        # opst: [stop, pots, tops]

        for key in anagrams.keys():
            result.append(anagrams[key])

        return result

