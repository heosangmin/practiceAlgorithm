'''
2022/05/25

https://programmers.co.kr/learn/courses/30/lessons/60060

'''
from bisect import bisect, bisect_left, bisect_right
def solution(words, queries):
    answer = []
    m = {}
    rm = {} # 와일드카드(?)가 접두사로 있을 경우에 word를 검색하기 위해 뒤집은 word의 리스트를 저장하는 맵
    
    # 단어 길이별로 리스트를 작성, 길이를 키로 맵에 추가
    for word in words:
        if len(word) not in m:
            m[len(word)] = []
            rm[len(word)] = []
        m[len(word)].append(word)
        rm[len(word)].append(word[::-1])
    
    # 리스트를 정렬(알파벳 오름차순으로)
    for k in m:
        m[k].sort()
        rm[k].sort()
    
    # 각 쿼리 검색
    for q in queries:
        key = len(q)
        if key not in m: # 해당 길이의 단어가 없으면 0
            answer.append(0)
            continue

        if q[0] != '?': # 접두사가 와일드카드(?)가 아닌 경우
            target_map = m
            target_query = q
        else:
            target_map = rm
            target_query = q[::-1]

        left = bisect_left(target_map[key], target_query.replace("?", "a"))
        right = bisect_right(target_map[key], target_query.replace("?", "z"))

        answer.append(right - left)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))