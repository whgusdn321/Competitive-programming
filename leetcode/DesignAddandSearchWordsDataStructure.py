class TrieNode:
    
    def __init__(self):
        self.children = [None]*27
        self.isEnd = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.s_word = None
        
    def idx(self, ch):
        return ord(ch) - ord('a')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
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
    
    def _search(self, start, i):
        runner = start
        n = len(self.s_word)
        
        for j in range(i, n):
            ch = self.s_word[j]
            if ch == '.':
                pos = False
                for child in runner.children:
                    if child:
                        pos |= self._search(child, j+1)
                return pos
            else:
                if runner.children[self.idx(ch)]:
                    runner = runner.children[self.idx(ch)]
                else:
                    return False
        return runner.isEnd

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.s_word = word
        return self._search(self.root, 0)
