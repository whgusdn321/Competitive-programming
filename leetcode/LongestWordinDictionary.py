from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(bool)
        self.isEnd = False
        
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.longest = []
        for word in words:
            self.add(word)
    
    def add(self, word):
        runner = self.root
        for i, ch in enumerate(word):
            if runner.children[ch]:
                runner = runner.children[ch]
            else:
                if i == len(word)-1:
                    newnode= TrieNode()
                    runner.children[ch] = newnode
                    runner = newnode
                else:
                    return 
        runner.isEnd = True       
        self.longest.append(word)
        # for child in runner.children.keys():
        #     self.longest.append(word+child)
    
    # def search(word):
        
        
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x:len(x))
        trie = Trie(words)
        trie.longest.sort(key=lambda x:(-len(x), x))
        print(trie.longest)
        return trie.longest[0]
        
