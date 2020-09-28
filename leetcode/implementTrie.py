class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    def idx(self, ch):
        return ord(ch) - ord('a')
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        runner = self.root
        for ch in word:
            if runner.children[self.idx(ch)]:
                runner = runner.children[self.idx(ch)]
            else:
                newNode = TrieNode()
                runner.children[self.idx(ch)] = newNode
                runner = newNode
                
        runner.isEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        runner = self.root
        pos = True
        for ch in word:
            if runner.children[self.idx(ch)]:
                runner = runner.children[self.idx(ch)]
            else:
                pos = False
                break
                
        if pos and runner.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        runner = self.root
        for ch in prefix:
            if runner.children[self.idx(ch)]:
                runner = runner.children[self.idx(ch)]
            else:
                return False
            
        return True 
