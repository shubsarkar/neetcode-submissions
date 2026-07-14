class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # need to understand how counting sort works
        left, right = 0, len(people) - 1
        boat_count = 0
        people.sort()
        # [1, 2, 4, 5], limit = 6
        # [1, 2, 2, 3, 3], limit = 3 

        while (left <= right):
            
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            
            boat_count += 1
        
        return boat_count
