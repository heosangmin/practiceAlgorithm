# 7장 연결리스트

리스트는 순서가 있는 값들의 모음(collection)을 구현하며, 반복이 포함될 수 있다. 단순 연결리스트(singly list)는 연속된 노드(node)로 이루어진 자료구조로, 각 노드(node)는 하나의 객체와 다음 노드에 대한 참조로 이루어져 있다. 첫 번째 노드는 헤드(head), 마지막 노드는 테일(tail)이라고 하고, 테일의 다음 노드는 null이 된다. 하지만 null 외에도 센티넬 노드(sentinel node) 혹은 자기 자신을 가리키는 방식으로 테일을 표현할 수 있다. 연결리스트에는 단순 연결리스트뿐만 아니라 다양한 방식의 연결리스트가 존재한다.

문제에 특별히 쓰여 있지 않다면, 이번 장에서 각 노드는 데이터와 다음 노드를 가리키는 참조 변수로 이루어져 있으며 마지막 노드의 참조 변수는 null을 가리킨다. 프로토타입은 다음과 같다.

```java
class ListNode<T> {
    public T data;
    public ListNode<T> next;
}
```

## 연결리스트 부트캠프
리스트 관련 문제는 두 가지 유형이 있는데, 리스트를 직접 구현하는 것과 표준 리스트 라이브러리를 사용하는 것으로 구분된다. 여기서는 두 가지 유형을 모두 다루는데, 먼저 구현 방법을 알아본 다음 리스트 라이브러리를 다룬다.

단순 연결리스트를 대상으로 기본적인 리스트 API(검색, 삽입, 삭제)를 구현해보는 것이 리스트에 익숙해지는 가장 좋은 방법이다.

### 키 검색하기
```java
public static ListNode<Integer> search(ListNode<Integer> L, int key) {
    while (L != null && L.data != key) {
        L = L.next;
    }
    return L;
}
```

### 특정 노드 다음에 새로운 노드를 삽입하기
```java
// node 다음에 newNode 삽입하기
public static void insertAfter(ListNode<Integer> node, ListNode<Integer> newNode) {
    newNode.next = node.next;
    node.next = newNode;
}
```

### 노드 삭제하기
```java
// aNode 바로 다음 노드 삭제하기, aNode는 테일이 아니라고 가정해도 된다.
public static void deleteList(ListNode<Integer> aNode) {
    aNode.next = aNode.next.next;
}
```

삽입과 삭제는 지역적으로 발생하는 연산이고 시간 복잡도는 O(1)이다. 검색은 모든 리스트를 순회해야 하므로 (키가 마지막 노드이거나 리스트에 존재하지 않는 경우) 시간 복잡도는 O(n)이 된다.(n은 전체 노드의 개수)

### 연결리스트 문제를 풀기 전 꼭 알고 있어야 할 내용
- 대부분의 리스트 문제는 O(n) 공간을 사용하는 무식하지만 간단한 해법이 존재한다. 하지만 **주어진 리스트 노드**를 사용해서 공간 복잡도는 O(1)로 줄이는 까다로운 해법도 존재한다. [문제 7.1, 문제 7.10]
- 리스트 문제는 대체로 개념적으로 간단하다. 새로운 알고리즘을 설계하는 것이라기보단 **깔끔한 코드**를 작성하는 것에 가깝다. [문제 7.12]
- 리스트가 비어 있는지 확인하는 작업은 번거롭다. **더미 헤드**(혹은 센티넬 노드)를 사용해 보라. [문제 7.2]
- 헤드와 테일에서 **다음 노드(이중 연결리스트에서는 이전 노드도)를 갱신하는 작업**은 빼먹기 쉬우므로 잊지 않도록 하자.[문제 7.10]
- 단순 연결리스트를 사용하는 알고리즘은 반복자를 두 개 사용하면 쉽게 풀리는 경우가 종종 있다. 하나의 반복자가 다른 반복자의 앞을 가리킨다든가 하나를 다른 하나보다 빠르게 움직여 볼 수 있다. [문제 7.3]

### 연결리스트 라이브러리 이해하기
표준 연결리스트 라이브러리를 살펴보자. 실제 면접에서는 여러분이 직접 리스트 클래스를 작성해야 한다는 사실을 명심하라.

동적으로 크기를 변경할 수 있는 배열이나 이중 연결리스트와 같이 순서가 있는 자료구조는 보통 List 인터페이스를 구현한다. List 인터페이스의 핵심 메서드는 add('A'), add(2, 3.14), addAll(C0), addAll(8, C), clear(), contains(2.71), get(12), indexOf(289), isEmpty(), iterator(), listIterator(), remove(1), removeAll(C), retainAll(C), set(3, 42), subList(1,5), toArray()가 있다. 반복자(iterator)를 사용하는 것에 익숙해져야 한다. 면접관이 요구할 때는 반복자 클래스를 직접 구현할 수 있어야 한다.

다음은 Java의 리스트를 사용할 때 염두에 두어야 할 사항들이다.

- List 인터페이스를 구현한 가장 흔한 클래스 두 개는 ArrayList(동적으로 크기를 조절할 수 있는 배열)와 LinkedList(이중 연결리스트로 구현되어 있다)이다. add(0, x)와 같은 연산은 ArrayList에서는 O(n) 시간이 걸리는데, LinkedList에서는 O(1) 시간이 걸린다. 이는 본질적으로 배열과 리스트의 성향이 다르기 때문이다.
- add(e)와 remove(idx)는 필수 메서드가 아니다. 특히 '5장 배열' 얘기했듯이 Arrays.asList()가 반환하는 객체는 이 메서드를 지원하지 않는다.

Java의 Collections 클래스는 컬렉션에서 작동하거나 컬렉션을 반환하는 정적 메서드로만 구성되어 있다. 몇 가지 유용한 메서드는 Collections.addAll(C, 1, 2, 4), Collections.binarySearch(list, 42), Collections.fill(list, 'f'), Collections.swap(C, 8, 1), Collections.min(C), Collections.min(C, cmp), Collections.max(C), Collections.max(C, cmp), Collections.reverse(list), Collections.rotate(list, 12), Collections.sort(list), Collections.sort(list, cmp)가 있다. 이 함수들은 간단해서 코딩 시간도 절약된다.

'5장 배열'에서 언급한 Arrays 클래스는 Arrays.asList()라는 정적 메서드를 가지고 있는데 이 메서드는 면접에서 굉장히 유용하다. Arrays.asList()는 스칼라 값을 인자에 넣을 수 있다. 예를 들어 Arrays.asList(1, 2, 4)는 1,2,4가 들어 있는 길이가 3인 리스트를 반환한다. 배열을 인자에 넣으면 O(1) 시간에 List 인터페이스를 구현한 객체를 만들어 준다.

Arrays.asList()는 튜플 클래스 혹은 접근자(getter)와 설정자(setter)를 직접 구현하기에 시간이 부족한 면접 환경에서 굉장히 유용하다. 효율적으로 튜플을 만들 수 있고, equals(), hashCode(), comparedTo()를 직접 구현하지 않아도 사용할 수 있다. 예를 들어, 간단한 2차원 데카르트 좌표 클래스를 구현하려면 25줄 정도의 코드를 작성해야 하는데 Arrays.asList(x1, y1)을 사용하면 그럴 필요가 없다.

다음은 Arrays.asList()에 대해 알고 있어야 할 몇 가지 사항이다.

- Arrays.asList(array)가 반환한 객체는 부분적으로 변경 가능하다. 이미 들어 있는 엔트리를 수정할 수 있지만 새로운 엔트리를 추가하거나 삭제할 수는 없다. 예를 들어 add(3.14)는 UnsupportedOperationException 오휴를 반환할 것이다. 하지만 기존 원소의 순서를 바꾸는 Collections.sort(Arrays.asList(array))는 오류가 발생하지 않는다. 왜냐하면 Arrays.asList(array)는 기존 배열 위에서 동작하는 어댑터를 반환하기 때문이다.
- Arrays.asList(new int[]{1, 2, 4})와 깉이 기본형 배열을 사용해서 Arrays.asList()를 호출하면, [1, 2, 4] 정수 배열이 들어 있는 노드가 하나뿐인 리스트가 반환될 것이다. 따라서 Arrays.asList(new Integer[]{1, 2, 4})와 같이 박스 타입을 사용해야 원하는 결과를 얻을 것이다.
- 기존 배열을 유지한 채 복사하려면 Arrays.copyOf(A, A.length)를 사용해야 한다.

## 7.1 두 개의 정렬된 리스트 합치기
단순 연결리스트 L과 F에 숫자가 오름차순으로 저장되어 있다고 가정하자. 우리는 L과 F를 합쳐서 하나의 단순 연결리스트로 표현하고자 한다. 단, 합쳐진 리스트의 숫자 또한 오름차순을 그대로 유지하고 싶다.

정렬된 단순 연결리스트 두 개가 주어졌을 때, 이 둘을 합친 리스트를 반환하는 프로그램을 작성하라. 여러분의 프로그램이 수정할 수 있는 변수는 다음 노드를 가리키는 next뿐이다.

> 힌트: 두 개의 정렬된 배열은 인덱스 두 개를 써서 합칠 수 있다. 리스트의 경우, 반복자가 끝에 도달했을 때의 처리에 주의하자.

단순하게 생각해보면 리스트 두 개를 합친 뒤 정렬하면 된다. 하지만 이 방법은 기존 리스트가 정렬되어 있다는 사실을 사용하지 않는다. 따라서 다시 정렬할 때 필요한 시간 복잡도는 O((n + m) log(n + m))이 된다(각 리스트의 길이를 n과 m이라 하자).

시간 복잡도 측면에서 더 효율적인 방법은 두 개의 리스트를 앞에서부터 확인하면서 작은 키를 가지고 있는 노드를 선택해 나가는 방법이다.

```java
public static ListNode<Integer> mergeTwoSortedLists(ListNode<Integer> L1, ListNode<Integer> L2) {
    // 결과를 저장할 변수를 생성한다.
    ListNode<Integer> dummyHead = new ListNode<>(0, null);
    ListNode<Integer> current = dummyHead;
    ListNode<Integer> p1 = L1, p2 = L2;

    while (p1 != null && p2 != null) {
        if (p1.data <= p2.data) {
            current.next = p1;
            p1 = p1.next;
        } else {
            current.next = p2;
            p2 = p2.next;
        }
        current = current.next;
    }

    // p1 혹은 p2에 남아 있는 노드를 덧붙인다.
    current.next = p1 != null ? p1 : p2;
    return dummyHead.next;
}
```

시간 복잡도 측면에서 최악의 경우의 시간 복잡도는 리스트의 길이와 같고 따라서 O(n + m)이 된다(최고의 경우는 리스트 하나가 다른 하나보다 굉장히 짧으면서 모든 노드가 합병된 리스트의 앞부분에 나타나는 경우일 것이다). 이미 존재하는 노드를 그대로 사용하므로 공간 복잡도는 O(1)과 같다.

