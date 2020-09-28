from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.children = defaultdict(bool)
        self.isEnd = False
        self.cnt = defaultdict(int)


class WordFilter:

    def __init__(self, words):
        self.root_pre = TrieNode()
        self.root_suf = TrieNode()

        for i, word in enumerate(words):
            self.add(word, i)
            self.add_rvs(word, i)

    def idx(self, ch):
        return ord(ch) - ord('a')

    def add(self, word, i):
        runner = self.root_pre
        n = len(word)
        for ch in word:
            # idx = self.idx(ch)
            if runner.children[ch]:
                runner = runner.children[ch]
                runner.cnt[n] += 1
            else:
                newNode = TrieNode()
                newNode.cnt[n] += 1
                runner.children[ch] = newNode
                runner = newNode
        runner.isEnd = True

    def add_rvs(self, word, i):
        rvs_word = word[::-1]
        runner = self.root_suf
        n = len(word)
        for ch in rvs_word:
            # idx = self.idx(ch)
            if runner.children[ch]:
                runner = runner.children[ch]
                runner.cnt[n] += 1
            else:
                newNode = TrieNode()
                newNode.cnt[n] += 1
                runner.children[ch] = newNode
                runner = newNode
        runner.isEnd = True

    def go_down(self, start, word):
        runner = start
        for ch in word:
            idx = self.idx(ch)
            if runner.children[ch]:
                runner = runner.children[ch]
            else:
                return None
        return runner

    def prefix(self, prefix, n):
        prefix_node = self.go_down(self.root_pre, prefix)
        if prefix_node:
            return prefix_node.cnt[n]
        else:
            return 0

    def suffix(self, suffix, n):
        suffix_node = self.go_down(self.root_suf, suffix[::-1])
        if suffix_node:
            return suffix_node.cnt[n]
        else:
            return 0


def solution(words, queries):
    answer = []
    dict1 = defaultdict(int)
    trie = WordFilter(words)
    for word in words:
        n = len(word)
        dict1[n] += 1

    for query in queries:
        n = len(query)
        num_q = 0
        if query[0] == '?':
            for i in range(n):
                if query[i] == '?':
                    num_q += 1
                else:
                    break
        else:
            for i in range(n - 1, -1, -1):
                if query[i] == '?':
                    num_q += 1
                else:
                    break
        if num_q == n:
            answer.append(dict1[n])
        elif query[0] == '?':
            valid = query[num_q:n]
            answer.append(trie.suffix(valid, n))
        else:
            valid = query[0:n - num_q]
            answer.append(trie.prefix(valid, n))
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))