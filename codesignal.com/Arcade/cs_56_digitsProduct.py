'''
2022/05/06

Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
solution(product) = 26;
For product = 19, the output should be
solution(product) = -1.
'''

'''
주어진 product를 곱하기로 만들 수 있는 숫자들의 조합 중 가장 작은 숫자를 반환하면 된다고 해석했다.
소수일 경우 -1를 반환한다.
'''
def solution(product):
    if product == 1:
        return product
    if product == 0:
        return 10

    # isPrime = True
    # for i in range(2, product):
    #     if product % i == 0:
    #         isPrime = False
    #         break
    
    # if isPrime:
    #     return -1

    # temp = []
    # f = 9
    # while f > 1:
    #     q,r = divmod(product, f)
    #     #print(product, q,r)
    #     f -= 1
    #     if r == 0:
    #         temp.append(f+1)
    #         product = q
    #         f = 9

    temp = []
    while product > 1:
        for f in range(9, 1, -1):
            if product % f == 0:
                product //= f
                temp.append(f)
                break
        else:
            return -1 # 소수일 경우
    
    return int("".join(map(str,sorted(temp))))

'''
몇 가지 테스트 케이스에서 풀리지 않는다.
다른 사람의 풀이를 보니 기본적인 방식은 같은데 반복문을 더 간단하게 할 수 있었다.
그리고 for else라는 구문도 처음 알았다.
'''

print(solution(12)) # 26
print(solution(19)) # -1
print(solution(243)) # 399
print(solution(360)) # 589
print(solution(0)) # 10
print(solution(1)) # 1
