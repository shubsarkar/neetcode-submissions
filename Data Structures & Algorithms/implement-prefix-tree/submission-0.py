class TrieNode:
    def __init__(self):
        # has map to map the chars to the next PrefixTree
        self.children = {}

        # bool flag to mark if a complete word ends at this exact node
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # word: apple
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]

        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]

        return True
        