class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        from collections import defaultdict
        from collections import deque

        adj_list = defaultdict(list)
        in_degree = defaultdict(int)

        output = []

        for word in words:
            for char in word:
                in_degree[char] = 0

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for (char1, char2) in zip(word1, word2):
                
                if char1 != char2:
                    adj_list[char1].append(char2)
                    in_degree[char2] += 1
                    break

        # initialize the queue with courses that has 0 dependencies
        queue = deque()
        for char in in_degree:
            if in_degree[char] == 0:
                queue.append(char)

        while queue:
            char = queue.popleft()
            output.append(char)

            for neighbor in adj_list[char]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(output) == len(in_degree):
            return "".join(output)
        else:
            return "" # a cycle was detected