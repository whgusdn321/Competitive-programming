from copy import deepcopy
from collections import deque

class Solution:
    
    def go(self, s, wordDict, i, memo):
        if i == len(s):
            return [deque([])]
        
        if memo[i] != -1:
            return deepcopy(memo[i])
        
        ret = []
        for word in wordDict:
            if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                results = self.go(s, wordDict, i+len(word), memo)
                for rett in results:
                    rett.appendleft(word)
                    ret.append(rett)
        memo[i] = ret
        return deepcopy(memo[i])
    
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = [-1 for _ in range(len(s))]
        strs = self.go(s, wordDict, 0, memo)
        ans = []
        for string in strs:
            s = ""
            for i, ss in enumerate(string):
                s += ss
                if i < len(string) - 1:
                    s += ' '
            ans.append(s)
        return ans
    
