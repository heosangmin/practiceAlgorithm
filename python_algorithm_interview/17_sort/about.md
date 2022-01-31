# 정렬 알고리즘

## 버블 정렬(Bubble Sort)

수도코드
```
Bubblesort(A)
    for i from 1 to A.length
        for j from 0 to A.length - 1
            if A[j] > A[j + 1]
                swap a[j] with a[j + 1]
```
O(n^2)의 복잡도를 가진다. 이 알고리즘은 n번의 라운드로 이루어져 있으며, 각 라운드마다 배열의 아이템을 한 번씩 쭉 모두 살펴본다. 연달아 있는 2개의 순서가 잘못되어 있다면 맞바꾼다.

```python
def bubblesort(A):
    for i in range(len(A)):
        for j in range(0, len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
```

## 병합 정렬(Merge Sort)
존 폰 노이만(John von Neumann)이 1945년에 고안한 알고리즘으로, 분할 정복(Divide and Conquer)의 진수를 보여주는 알고리즘이다. 최선, 최악 모두 O(n log n)으로 일정한 알고리즘이며, 대부분의 경우 퀵 정렬보다는 느리지만 일정한 실행 속도뿐만 아니라 무엇보다도 안정 정렬(Stable Sort)라는 점에서 여전히 사용 라이브러리에 많이 쓰이고 있다.

## 퀵 정렬(Quick Sort)
토니 호어(Tony Hoare)가 1959년에 고안한 알고리즘으로, 피벗을 기준으로 좌우를 나누는 특징 때문에 파티션 교환 정렬(Partition-Exchange Sort)라고도 불리운다. 병합 정렬과 마찬가지로 분할 정복 알고리즘이며 여기에 피벗(Pivot)이라는 개념을 통해 피벗보다 작으면 왼쪽, 크면 오른쪽과 같은 방식으로 파티셔닝하면서 쪼개 나간다.

수도코드(로무토 파티션 계획)
```
Quicksort(A, lo, hi)
    if lo < hi then
        pivot := partition(A, lo, hi)
        Quicksort(A, lo, pivot - 1)
        Quicksort(A, pivot + 1, hi)

partition(A, lo, hi)
    pivot := A[hi]
    i := lo
    for j := lo to hi do
        if A[j] < pivot then
            swap A[i] with A[j]
            i := i + 1
    swap A[i] with A[hi]
    return i
```

여기서 partition()은 로무토 파티션으로, 맨 오른쪽을 피벗으로 정하는 가장 단순한 방식이다. 피벗은 맨 오른쪽 값을 기준으로 하며, 이를 기준으로 2개의 포인터가 이동해서 오른쪽 포인터의 값이 피벗보다 작다면 서로 스왑하는 형태로 진행된다.

```python
def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)

```

만약 정렬된 배열이 입력된다면 최악의 경우로서 O(n^2)이다. 이 경우 피벗이 계속 오른쪽에 위치하게 되므로 파티셔닝이 전혀 이루어지지 않는다. 퀵 정렬은 입력값에 따라 성능 편차가 심한 편이다.

### 안정 정렬 vs. 불안정 정렬
> 안정 정렬(Stable Sort) 알고리즘은 중복된 값을 입력 순서와 동일하게 정렬한다.

안정 정렬
- 병합 정렬
- 버블 정렬

불안정 정렬
- 퀵 정렬

퀵 정렬은 고르지 않은 성능 탓에 실무에서는 병합 정렬이 여전히 활발이 쓰이고 있으며(라고 책에 적혀 있음), 파이썬의 기본 정렬 알고리즘으로는 병합 정렬과 삽입 정렬을 휴리스틱하게 조합한 팀소트(Timsort)를 사용한다.