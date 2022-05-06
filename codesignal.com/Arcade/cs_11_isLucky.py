def solution(n):
    n = str(n)
    return sum(int(i) for i in n[:len(n)//2]) == sum(int(i) for i in n[len(n)//2:len(n)])

n = 1230
print(solution(n))

n = 239017
print(solution(n))