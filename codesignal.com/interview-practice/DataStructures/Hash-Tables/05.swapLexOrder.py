'''
2022/06/06

https://app.codesignal.com/interview-practice/task/5vXzdE9yzjsoMZ9sk

Given a string str and array of pairs that indicates which indices in the string can be swapped, return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.

Example

For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
solution(str, pairs) = "dbca".

By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca". The lexicographically largest string in this list is "dbca".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string str

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ str.length ≤ 104.

[input] array.array.integer pairs

An array containing pairs of indices that can be swapped in str (1-based). This means that for each pairs[i], you can swap elements in str that have the indices pairs[i][0] and pairs[i][1].

Guaranteed constraints:
0 ≤ pairs.length ≤ 5000,
pairs[i].length = 2.

[output] string
'''

def solution(str, pairs):
    if not str or not pairs:
        return ('', str)[not pairs]
    lst = [''] + list(str)
    setted_pairs = list(map(set, pairs))
    while setted_pairs:
        path = setted_pairs.pop(0) # 앞에서부터 페어를 하나씩 꺼냄
        while True:
            path_copy = path.copy() # 꺼낸 페어의 복사본을 만듦
            for pair in setted_pairs: # 나머지 페어들을 하나씩 반복하며
                if pair & path_copy: # 꺼낸 페어와 교집합(공통 요소)이 있을 경우
                    path |= pair # 두 페어를 합침
                    setted_pairs.remove(pair)
            #print(path)
            if path == path_copy:
                break
        optimal = sorted(lst[i] for i in path)
        #print(optimal)
        for i, v in enumerate(sorted(path, reverse=True)):
            lst[v] = optimal[i]
        return ''.join(lst[1:])

def solution(str, pairs):
    if not str or not pairs:
        return ('', str)[not pairs]
    lst = [''] + list(str)
    setted_pairs = list(map(set, pairs))
    while setted_pairs:
        path = setted_pairs.pop(0)
        while True:
            path1 = path.copy()
            for pair in setted_pairs:
                if path1 & pair:
                    path |= pair
                    setted_pairs.remove(pair)
            if path == path1:
                break
        optimal = sorted(lst[i] for i in path)
        for i, v in enumerate(sorted(path, reverse=True)):
            lst[v] = optimal[i]
    return ''.join(lst[1:])

print(solution(str = "abdc", pairs = [[1, 4], [3, 4]])) # "dbca"