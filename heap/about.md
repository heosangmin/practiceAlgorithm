# Heap
- 힙은 힙의 특성(최소 힙 Min Heap 에서는 부모가 항상 자식보다 작거나 같다)을 만족하는 거의 완전한 트리(Almost Complete Tree)인 특수한 트리 기반의 자료구조다.
- 파이썬의 heapq 모듈이 힙으로 구현되어 있다.
- 파이썬에서는 최소 힙만 구현되어 있다.
- 최소 힙은 부모가 항상 자식보다 작기 때문에 루트가 결국 가장 작은 값을 갖게 된다.
- 우선순위 큐 ADT(추상 자료형)은 주로 힙으로 구현하고, 힙은 주로 배열로 구현한다. 따라서 우선순위 큐는 결국은 배열로 구현하는 셈이 된다.
- 힙은 정렬된 구조가 아니다.
- 자식이 둘인 힙은 이진 힙(Binary Heap)이라고 한다.

## 구현
```python
class BinaryHeap(object):
    
    def __init__(self):
        self.items = [None]
    
    def __len__(self):
        return len(self.items) - 1
```

### 삽입
1. 요소를 가장 하위 레벨의 최대한 왼쪽으로 삽입한다(배열로 표현할 경우 가장 마지막에 삽입한다).
2. 부모 값과 비교해 값이 더 작은 경우 위치를 변경한다.
3. 계속해서 부모값과 비교해 위치를 변경한다(가장 작은 값일 경우 루트까지 올라감).

```python
    def _percolate_up(self):
        i = len(self) # 배열 인덱스 0이 None으로 시작하므로 마지막 요소의 인덱스는 배열의 길이와 일치함
        parent = i // 2 # 이진 트리 특성상 부모 노드의 인덱스는 자식 노드 인덱스를 2로 나눈 수가 됨
        while parent >= 0:
            if self.items[i] < self.items[parent]: # 부모가 더 크다면
                self.items[parent], self.items[i] = self.items[i], self.items[parent] # 스왑
            i = parent
            parent = i // 2
            
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()
```

### 추출
루트를 추출하면 된다. 복잡도가 O(1)은 아닌 이유는 추출 이후에 힙의 특성을 유지하는 작업이 필요하기 때문에 O(log n)이다.

1. 루트를 추출한다.
2. 마지막 요소를 루트로 이동한다.
3. (삽입과는 반대로) 루트와 그 자식 노드를 비교해서 자식보다 크다면 스왑하며 내려가는 다운힙(Down Heap)을 수행한다.

```python
    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)
    
    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted
```
