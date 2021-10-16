'''
819. Most Common Word

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
'''

from typing import List
import re
from collections import Counter
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # d = defaultdict(int)
        # for word in re.sub(r'[^\w\s]','',paragraph).split():
        #     if word.lower() not in banned: 
        #         d[word.lower()] += 1
        # return max(d, key=d.get)

        words = [word for word in re.sub(r'[^\w\s]','',paragraph).lower().split() if word not in banned]
        counts = Counter(words)
        return counts.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

s = Solution()
print(s.mostCommonWord(paragraph, banned))