from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        pattern_map = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]

                for next_word in pattern_map[pattern]:

                    if next_word == endWord:
                        return level + 1

                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))

                # Important: don't process the same pattern again
                pattern_map[pattern] = []

        return 0
    
    
s = Solution()
# Example usage:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
result = s.ladderLength(beginWord, endWord, wordList)
print("The length of the shortest transformation sequence is:", result)