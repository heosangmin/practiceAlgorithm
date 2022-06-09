'''
2022/06/09

https://app.codesignal.com/interview-practice/task/Ki9zRh5bfRhH6oBau

You have two arrays of strings, words and parts. Return an array that contains the strings from words, modified so that any occurrences of the substrings from parts are surrounded by square brackets [], following these guidelines:

If several parts substrings occur in one string in words, choose the longest one. If there is still more than one such part, then choose the one that appears first in the string.

Example

For words = ["Apple", "Melon", "Orange", "Watermelon"] and parts = ["a", "mel", "lon", "el", "An"], the output should be
solution(words, parts) = ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"].

While "Watermelon" contains three substrings from the parts array, "a", "mel", and "lon", "mel" is the longest substring that appears first in the string.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string words

An array of strings consisting only of uppercase and lowercase English letters.

Guaranteed constraints:
0 ≤ words.length ≤ 104,
1 ≤ words[i].length ≤ 30.

[input] array.string parts

An array of strings consisting only of uppercase and lower English letters. Each string is no more than 5 characters in length.

Guaranteed constraints:
0 ≤ parts.length ≤ 105,
1 ≤ parts[i].length ≤ 5,
parts[i] ≠ parts[j].

[output] array.string
'''

# 이걸 트리로 풀려고 하니 감이 오지 않는다. 트라이인가?
# 그냥 구현으로 풀고 다른 사람들의 풀이를 확인하자.
# def solution(words, parts):
#     print(sorted(parts, key=len, reverse=True))
#     for i in range(len(words)):
#         for part in sorted(parts, key=len, reverse=True):
#             if words[i].find(part) > -1:
#                 words[i] = words[i].replace(part, "[" + part + "]", 1)
#                 break
#     return words

# 유저[k_lee]의 풀이를 보니 트라이로 풀고 있었다.
class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

    def add(self, word):
        if not word:
            self.end = True
        else:
            self.children.setdefault(word[0], TrieNode()).add(word[1:])

def solution(words, parts):
    trie = TrieNode()

    for part in parts:
        trie.add(part)

    for i, word in enumerate(words):
        pos = len(word)
        len_of_word_sub = -1
        for j in range(len(word)):
            local_trie = trie
            k = j
            while k < len(word) and word[k] in local_trie.children:
                local_trie = local_trie.children[word[k]]
                k += 1
                if local_trie.end and k - j > len_of_word_sub:
                    len_of_word_sub = k - j
                    pos = j
        if len_of_word_sub > 0: # if word has part
            words[i] = word[:pos] + "[" + word[pos:pos+len_of_word_sub] + "]" + word[pos+len_of_word_sub:]
    return words

words = ["Apple", "Melon", "Orange", "Watermelon"]
parts = ["a", "mel", "lon", "el", "An"]
print(solution(words, parts)) # ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"]

words = ["neuroses", "myopic", "sufficient", "televise", "coccidiosis", "gules", "during", "construe", "establish", "ethyl"]
parts = ["aaaaa", "Aaaa", "E", "z", "Zzzzz", "a", "mel", "lon", "el", "An", "ise", "d", "g", "wnoVV", "i", "IUMc", "P", "KQ", "QfRz", "Xyj", "yiHS"]
print(solution(words, parts))