'''
336. Palindrome Pairs
https://leetcode.com/problems/palindrome-pairs/

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:
Input: words = ["a",""]
Output: [[0,1],[1,0]]

Constraints:
1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
'''

from typing import List
import collections

class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word) -> bool:
        return word == word[::-1]

    def insert(self, index: int, word: str) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                '''
                판별 로직 2
                삽입 중에 "남아 있는 단어"가 팰린드롬이면
                미리 팰린드롬 여부를 세팅함.(palindrome_word_ids)
                '''
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index: int, word: str) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            '''
            판별 로직 3
            탐색 중간에 word_id가 있고 나머지 문자가 팰린드롬인 경우
            '''
            if node.word_id >= 0:
                '''
                단어를 뒤집어서 구축한 트라이이기 때문에
                입력값은 순서대로 탐색하다가,
                끝나는 지점의 word_id 값이 -1이 아니라면,
                현재 인덱스 index와 해당 word_id는 팰린드롬으로 판단할 수 있다.
                '''
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
                    print("#3", word, index, node.word_id)

            if not word[0] in node.children:
                return result

            node = node.children[word[0]]
            word = word[1:]

        '''
        판별 로직 1
        끝까지 탐색했을 때 word_id가 있는 경우
        '''
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
            print("#1", word, index, node.word_id)

        '''
        판별 로직 2
        끝까지 탐색했을 때 palindrome_word_ids가 있는 경우
        '''
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
            print("#2", word, index, palindrome_word_id)

        return result

class Solution:
    def palindromePairs1(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]
        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i,j])

        return output

    def palindromePairs2(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)
        
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
        
        return results

s = Solution()

words1 = ["abcd","dcba","lls","s","sssll"]
words2 = ["bat","tab","cat"]
words3 = ["a",""]
words4 = ['d', 'cbbcd', 'dcbb', 'dcbc', 'cbbc', 'bbcd']

# print(words1)
# print(words2)
# print(words3)
print(words4)

# print(s.palindromePairs1(words1))
# print(s.palindromePairs1(words2))
# print(s.palindromePairs1(words3))

# print(s.palindromePairs2(words1))
# print(s.palindromePairs2(words2))
# print(s.palindromePairs2(words3))
print(s.palindromePairs2(words4))