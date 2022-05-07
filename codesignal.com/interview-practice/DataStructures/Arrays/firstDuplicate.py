'''
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 1, 3, 5, 3, 2], the output should be solution(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be solution(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be solution(a) = -1.
'''

'''
문제를 단순하게 볼 줄 알아야한다.
중복된 요소가 처음 나왔다면 그녀석이 답이잖아.
'''

def solution(a):
    s = set()
    for e in a:
        if e in s:
            return e
        s.add(e)
    return -1
    # index = 10001
    # for i in range(len(a)-1):
    #     for j in range(i+1,len(a)):
    #         if a[i] == a[j]:
    #             index = min(j, index)
    #             break
    #     if i > index:
    #         break
    # if index > 10000:
    #     return -1
    # return a[index]

print(solution([2, 1, 3, 5, 3, 2])) # 3
print(solution([8, 4, 6, 2, 6, 4, 7, 9, 5, 8])) # 6