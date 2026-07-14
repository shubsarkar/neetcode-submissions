class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_interval = intervals[i]

            # compare the current with the last one in merged
            last_merged = merged[-1]

            # current end time is greater than merged end time, no overlap
            if current_interval[0] > last_merged[1]:
                # they dont overlap
                merged.append(current_interval)
            # otherwise, we update the end time of last merged interval
            else:
                last_merged[1] = max(last_merged[1], current_interval[1])

        return merged
