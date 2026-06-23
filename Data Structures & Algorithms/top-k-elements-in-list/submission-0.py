class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {} 
        '''
        number: frequency
        {1: 1, 2: 2, 3: 3}
        '''
        freq = [[] for i in range(len(nums) + 1)]
        '''
        idx : [list]
        [0: [], 1: [1], 2: [2], 3: [3], 4: [], 5: [], 6: []]
        '''

        result = []

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for n, c in counts.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result


            


        
        

        