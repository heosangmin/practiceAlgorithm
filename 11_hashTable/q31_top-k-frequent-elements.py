'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 105
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.
'''

# 책이 엉망이다.
# 307페이지에 나온 문제 "k번 이상 등장하는 요소를 추출하라."는 잘못된 해석이다.
# "k most frequent elements"는 k번 이상 등장하는 요소가 아니라 "가장 많이 등장하는 k가지의 요소"가 맞는 해석이다.
# k번 이상 등장하는 요소라면 매우 쉽게 풀리는데 실제 리트코드에 업로드 해보니 nums=[1,2], k=2의 기대값이 [1,2]라고 한다.
# k번 이상 등장이니 2번 이상 등장하는 요소가 없으므로 []가 답이지 않은가. 그래서 원문을 다시 읽어보니 k most frequent elements였다.
# 이사람은 뭐가 문제야 도대체. 본인이 직접 다 풀어 본건지 뭔지 의심스러울 정도.
# 게다가 문제를 풀기 위한 알고리즘에 어떻게 접근해야하는지를 보여주지도 않고 그냥 풀이만 있음.
# 역시나 오만한 책이다.

import collections
from typing import List
from collections import defaultdict, Counter
import heapq

class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        '''
        생각나는대로 풀이
        해시테이블(딕셔너리)에 요소별 등장 횟수를 저장하고
        리스트로 옮긴 뒤 등장 횟수의 역순으로 정렬해 k번 추출한 결과를 반환
        '''
        freqs = defaultdict(int)
        freqs_list = []
        result = []
        for num in nums:
            freqs[num] += 1
        for num in freqs:
            freqs_list.append((freqs[num], num))
        freqs_list.sort(key=lambda x: (-x[0]))
        for i in range(k):
            result.append(freqs_list[i][1])
        return result

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        '''
        책 풀이 1번
        '''
        freqs = Counter(nums)
        freqs_heap = []
        
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        
        topk = []
        # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk

    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]


nums1 = [1,1,1,2,2,3]
k1 = 2
nums2 = [1]
k2 = 1

solution = Solution()
# print(solution.topKFrequent1(nums1, k1))
# print(solution.topKFrequent1(nums2, k2))
# print(solution.topKFrequent2(nums1, k1))
# print(solution.topKFrequent2(nums2, k2))
print(solution.topKFrequent3(nums1, k1))
print(solution.topKFrequent3(nums2, k2))