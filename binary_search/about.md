# 이진 검색
> 이진 검색(Binary Search)이란 정렬된 배열에서 타겟을 찾는 검색 알고리즘이다.

이진 검색은 값을 찾아내는 시간 복잡도가 O(log n)이라는 점에서 대표적인 로그 시간 알고리즘이며, 이진 탐색 트리(Binary Search Tree)와도 유사한 점이 많다.

```
function binary_search(A, n, T) is
    L := 0
    R := n - 1
    while L <= R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m - 1
        else:
            return m
    return unsuccessful
```
