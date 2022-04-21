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

## 7.2 부분 리스트 하나 뒤집기
리스트의 부분 리스트를 역순으로 재배열하는 문제를 풀어보자.

단순 연결리스트 L과 두 개의 정수 s와 f가 주어졌을 때 s번째 노드부터 f번째 노드까지 뒤집는 프로그램을 작성하라. 단, 헤드 노드를 시작으로 1부터 차례대로 번호를 매긴하고 가정하자. 이때 노드를 추가해선 안 된다.

> 힌트: 갱신해야 할 다음 노드를 주의 깊게 살펴보자.

직접적인 해법은 부분 리스트를 뽑아낸 뒤, 뒤집고, 기존 기존 리스트에 이어서 붙여 주면 된다. 하지만 이 경우에는 부분 리스틀 두 번 읽어야 하는 단점이 있다.

하지만 부분 리스트를 찾는 동시에 뒤집을 수 있다면 어떨까? 부분 리스트를 한 번만 읽어서 문제를 해결할 수 있을 것이다. 리스트를 앞에서부터 차례로 훑어 가면서 부분 리스트의 시작 지점을 찾는다. s번째 노드에 도착하면 부분 리스트의 시작 노드와 이전 노드가 무엇인지 알 수 있다. 이제 뒤집는 과정을 시작하는 동시에 계속 리스트의 앞으로 나아간다. f번쨰 노드에 도착한 후 뒤집는 과정을 멈춘다. 그 다음에 뒤집은 부분 리스트를 기존 리스트에 연결시킨다.

```java
public static ListNode<Integer> reverseSublist(ListNode<Integer> L, int start, int finish) {
    if (start == finish) {
        return L;
    }

    ListNode<Integer> dummyHead = new ListNode<>(0, L);
    ListNode<Integer> sublistHead = dummyHead;
    int k = 1;
    while (k++ < start) {
        sublistHead = sublistHead.next;
    }

    // 부분 리스트를 뒤집는다.
    ListNode<Integer> sublistIter = sublistHead.next;
    while (start++ < finish) {
        ListNode<Integer> temp = sublistIter.next;
        sublistIter.next = temp.next;
        temp.next = sublistHead.next;
        sublistHead.next = temp;
    }
    return dummyHead.next;
}
```

f번째 노드까지만 순회하면 되므로 시간 복잡도는 O(f)가 된다.

## 7.3 사이클이 존재하는지 확인하기
마지막 노드가 null로 끝나는 노드의 시퀀스를 일컬어 연결리스트(linked list)라고 부르지만, next 필드에 이전 노드를 가리키면 사이클이 형성될 수도 있다.

단순 연결리스트의 헤드가 주어졌을 때 사이클이 존재하면 사이클의 시작 노드를, 그렇지 않으면 null을 반환하는 프로그램을 작성하라(단, 리스트의 길이를 사전에 알 수 없다).

> 힌트: 두 개의 반복자를 사용해서 하나는 빠르게 하나는 느리게 움직여 보자.

이 문제에는 여러가지 해법이 존재한다. 공간에 제약이 없다면 간단하게 방문했던 노드들을 전부 해시 테이블에 넣고 현재 노드가 이전에 방문했던 노드인지에 따라 사이클의 존재 유무를 확인할 수 있다. 사이클이 존재하지 않는다면 탐색은 테일에서 끝날 것이다(테일은 종종 next를 null로 세팅한다). 전체 노드의 개수를 n이라 할 때 이 방법은 O(n)의 공간을 추가적으로 사용해야 한다.

추가적인 공간 없이 생각해 보자. 무식하게 생각해 보면 이중 루프를 사용해 볼 수 있다. 바깥 루프는 리스트의 노드를 하나씩 방문하고, 안쪽 루프는 매번 헤드에서 시작해서 바깥 루프가 가리키는 노드까지 반복한다. 바깥 루프가 방문했던 노드를 안쪽 루프가 재방문 했다면 사이클이 존재한다고 말할 수 있다. 혹은 바깥 루프가 리스트의 끝에 도달했다면 사이클이 없다고 말할 수 있다. 이 방법의 시간 복잡도는 O(n^2)이다.

이 아이디어를 발전시켜 선형 시간에 문제를 풀어 보자. 두 개의 반복자를 사용할 것이다. 하나는 천천히 움직이고, 다른 하나는 빠르게 움직이며 리스트를 순회한다. 즉, 단계마다 천천히 움직이는 반복자는 노드를 한 개씩 방문하고, 빠르게 움직이는 반복자는 노드를 두 개씩 방문한다. 만약 두 반복자가 어느 순간 같은 노드를 가리킨다면 사이클이 존재한다고 말할 수 있다. 왜냐하면 빠르게 움직이는 반복자가 느리게 움직이는 반복자를 건너뛴다면, 그 다음 단계에 두 반복자는 만나게 되어 있기 때문이다.

이 방법을 통해 사이클의 유무를 찾을 수 있다. 사이클의 시작 지점은 사이클의 길이 C를 통해 구할 수 있다. 사이클이 존재하고 현재 가리키는 노드가 사이클 내부에 있다면, 사이클의 길이를 쉽게 구할 수 있다. 사이클의 첫 번째 노드를 찾기 위해서 두 개의 반복자가 필요하다. 하나를 다른 하나보다 C만큼 앞서 배치한 뒤, 그 둘을 동시에 한 칸씩 움직이다 보면 언젠가는 둘이 만나게 된다. 그 만나는 지점이 사이클의 첫 번째 노드가 된다.

```java
public static ListNode<Integer> hasCycle(ListNode<Integer> head) {
    ListNode<Integer> fast = head, slow = head;

    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            // 사이클이 존재한다면, 사이클의 길이를 계산한다.
            int cycleLen = 0;
            do {
                ++cycleLen;
                fast = fast.next;
            } while (slow != fast);

            // 사이클의 시작 지점을 찾는다. ???
            ListNode<Integer> cycleLenAdvancedIter = head;

            // cycleLenAdvancedIter 포인터를 cycleLen 길이만큼 앞으로 보낸다. ???
            while (cycleLen-- > 0) {
                cycleLenAdvancedIter = cycleLenAdvancedIter.next;
            }

            ListNode<Integer> iter = head;
            // 두 반복자를 같이 움직인다.
            while (iter != cycleLenAdvancedIter) {
                iter = iter.next;
                cycleLenAdvancedIter = cycleLenAdvancedIter.next;
            }
            return iter; // iter가 사이클의 시작 지점이다.
        }
    }
    return null; // 사이클이 없다.
}
```

사이클의 시작 지점까지의 노드의 개수를 F, 사이클의 길이를 C, 전체 노드의 개수를 n이라고 할 때 시간 복잡도는 O(F) + O(C) = O(n)이 된다. 두 반복자가 사이클 내부로 들어가는 데 O(F)가 소요되고, 사이클 내부에서 두 반복자가 만나는 데 O(C)가 소요된다.

> 응용: 다음은 사이클의 길이를 계산하지 않고 사이클의 시작점을 찾는 프로그램이다. 이 프로그램은 앞의 코드보다 더 간결하다. 프로그램이 제대로 동작하는지 확인해 보자.

```java
public static ListNode<Integer> hasCycle(ListNode<Integer> head) {
    ListNode<Integer> fast = head, slow = head;

    while (fast != null && fast.next != null && fast.next.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) { // 사이클이 존재한다.
            // 사이클의 시작 지점을 찾는다.
            slow = head;
            // 동시에 두 포인터를 앞으로 내보낸다.
            while (slow != fast) {
                slow = slow.next;
                fast = fast.next;
            }
            return slow; // slow가 사이클의 시작 지점이다.
        }
        return null; // 사이클이 존재하지 않는다.
    }
}
```

## 7.4 사이클이 없는 두 리스트가 겹치는지 확인하기
두 개의 단순 연결리스트가 동일한 노드 리스트를 공유할 수도 있다. 플라이웨이트 패턴(flyweight pattern)을 통해 메모리 공간을 절약할 목적이 있을 수도 있고, 정규 형태를 유지하려는 목적이 있을 수도 있다.

사이클 없는 단순 연결리스트 두 개가 주어졌을 때 두 리스트가 노드를 공유하는지 판단하는 프로그램을 작성하라.

> 힌트: 단순한 경우를 먼저 생각해 보자.

무식한 방법으로 생각해 보면 하나의 리스트에 있는 노드를 전부 해시 테이블에 넣고 해당 노드가 해시 테이블에 존재하는지 확인해 보면 된다. 이 방식을 모든 노드에 대해서 반복한다. 전체 노드가 n개일 때 O(n)의 공간과 시간이 필요하다.

이중 루프를 이용하면 공간을 추가로 사용하지 않을 수도 있다. 즉, 하나는 첫 번째 리스트를 반복하고 다른 하나는 두 번째 리스트를 반복하면서 두 번째 리스트의 노드가 첫 번째 리스트에 포함되어 있는지 확인한다. 이 방법은 O(n^2) 시간이 소요된다.

여기에 중요한 사실이 하나 있다. 서로 겹치는 리스트는 반드시 테일을 공유해야 한다는 것이다. 즉, 리스트가 중간에 한 번 만나면 다시 갈라질 수 없다. 따라서 각 리스트의 테일만 확인하면 두 리스트가 겹치는지 확인할 수 있다.

겹치는 두 리스트가 처음으로 공유하는 노드를 찾으려면 어떻게 해야 할까? 우선 두 리스트의 길이를 알아야 한다. 그다음 길이가 짧은 리스트는 헤드에서 시작하고, 길이가 긴 리스트는 두 리스트 길이의 차이만큼 앞에서 시작해서 같이 한 칸씩 나아간다. 그러면 처음으로 공유하는 노드에서 만나게 된다. 만약 공통된 노드를 끝까지 찾지 못했다면 두 리스트가 공유하는 노드는 없다는 뜻이다.

```java
public static ListNode<Integer> overlappingNoCycleLists(ListNode<Integer> L1, ListNode<Integer> L2) {
    int L1Length = length(L1), L2Length = length(L2);

    // 두 리스트의 길이가 같아지도록 길이가 긴 리스트를 먼저 앞으로 내보낸다.
    if (L1Length > L2Length) {
        L1 = advanceListByK(L1Length - L2Length, L1);
    } else {
        L2 = advanceListByK(L2Length - L1Length, L2);
    }

    while (L1 != null && L2 !== null L1 != L2) {
        L1 = L1.next;
        L2 = L2.next;
    }
    return L1; // L1과 L2가 겹치지 않으면 null을 반환?
}

public static ListNode<Integer> advanceListByK(int k, ListNode<Integer> L) {
    while (k-- > 0) {
        L = L.next;
    }
    return L;
}

private static int length(ListNode<Integer> L) {
    int len = 0;
    while (L != null) {
        len++;
        L = L.next;
    }
    return len;
}
```

이 알고리즘의 시간 복잡도는 O(n)이고 공간 복잡도는 O(1)이다.

## 7.5 사이클이 존재하는 두 리스트가 겹치는지 확인하기
문제 7.4를 약간 변형해 보자. 만약 사이클을 포함하는 리스트도 존재한다면 공유하는 노드를 어떻게 찾아야 할까? 만약 공유하는 노드가 존재한다면, 가장 처음 만나는 노드를 반환하면 된다. 하지만 처음 만나는 노드가 여러 개일 가능성이 있다. 만약 노드가 사이클에 포함되어 있다면 두 리스트에 포함된 사이클이 같더라도, 첫 번째 리스트를 순회하면서 찾은 첫 번째 겹치는 노드와 두 번째 리스트를 순회하면서 찾은 첫 번째 겹치는 노드가 다를 수 있다. 이 경우에는 두 노드 중 아무거나 반환하면 된다.

> 힌트: 케이스를 분석해 보라. 두 리스트 모두 사이클이 있으면 어떻게 해야 할까? 같은 사이클로 끝나는 경우에는 어떻게 해야 할까? 하나는 사이클이 있지만 다른 하나는 사이클이 없다면 어떻게 해야 할까?

이 문제는 문제 7.4의 해법에서 언급했던 해시 테이블을 사용하면 쉽게 풀 수 있다. 이 방법은 전체 노드가 n개일 때 시간 복잡도와 공간 복잡도가 모두 O(n)이 된다.

다양한 케이스를 고려해 보면 공간 복잡도를 개선할 수 있다. 가장 쉬운 케이스는 사이클이 없는 경우로 문제 7.3의 해법을 사용해서 해결할 수 있다. 이 케이스는 문제 7.4의 해법을 사용해서 겹치는지 확인하면 된다.

만약 하나는 사이클이 존재하고 다른 하나는 사이클이 존재하지 않는다면 이 두 리스트는 공유하는 노드가 있을 수 없다.

이제 두 리스트 모두 사이클이 존재하는 경우를 생각해 보자. 두 리스트가 겹친다면, 두 리스트의 사이클은 반드시 동일해야 한다.

두 가지 경우의 수가 존재한다. 첫 번째 경우는 사이클이 시작되기 전에 만나는 경우인데, 이 경우에는 둘이 만나는 첫 번째 노드가 단 하나여야 한다. 두 번째 경우는 사이클이 시작된 후에 만나는 경우이다. 첫 번째 경우는 문제 7.4의 해법을 이용해서 풀 수 있고, 두 번째 경우는 문제 7.3의 해법을 사용해서 풀 수 있다.

```java
public static ListNode<Integer> overlappingLists(ListNode<Integer> L1, ListNode<Integer> L2) {
    // 사이클의 시작 지점을 저장한다.
    ListNode<Integer> root1 = CheckingCycle.hasCycle(L1);
    ListNode<Integer> root2 = CheckingCycle.hasCycle(L2);

    if (root1 == null && root2 == null) {
        // 두 리스트 모두 사이클이 존재하지 않는다.
        return overlappingNoCycleLists(L1, L2);
    } else if ((root1 != null && root2 == null) || (root1 == null && root2 != null)) {
        // 하나는 사이클이 존재하고 하나는 존재하지 않는다.
        return null;
    }

    // 두 리스트 모두 사이클이 존재한다.
    ListNode<Integer> temp = root2;
    do {
        temp = temp.next;
    } while ( temp != root1 && temp != root2 );

    // L1과 L2가 같은 사이클에서 끝나지 않는다.
    if (temp != root1) {
        return null; // 사이클이 겹치지 않는다.
    }

    // L1과 L2가 같은 사이클로 끝난다.
    // 사이클이 시작하기 전에 첫 번째 노드가 겹친다면 그 위치를 가리키게 한다.
    int stem1Length = distance(L1, root1), stem2Length = distance(L2, root2);
    if (stem1Length > stem2Length) {
        L1 = OverlappingListNoCycle.advanceListByK(stem1Length - stem2Length, L1);
    } else {
        L2 = OverlappingListNoCycle.advanceListByK(stem2Length - stem1Length, L2);
    }

    while (L1 != L2 && L1 != root1 && L2 != root2) {
        L1 = L1.next;
        L2 = L2.next;
    }

    // 만약에 root1에 도달하기 전에 L1 == L2이 되었다면, 첫 번째로 겹치는 노드가
    // 사이클이 시작하기 전이라는 의미이다. 그게 아니라면, 처음으로 겹치는 노드는
    // 여러 개 존재할 수 있고 사이클 내에 있는 아무 노드나 반환하면 된다.
    return L1 == L2 ? L1 : root1;
}

// a와 b 사이의 거리를 계산한다.
private static int distance(ListNode<Integer> a, ListNode<Integer> b) {
    int dis = 0;
    while (a != b) {
        a = a.next;
        ++dis;
    }
    return dis;
}
```

n과 m을 입력 리스트의 길이라고 했을 때, 시간 복잡도는 O(n + m)이고 공간 복잡도는 O(1)이다.

## 7.6 단순 연결리스트에서 노드 삭제하기
일반적으로 단순 연결리스트의 어떤 노드가 주어졌을 때 이 노드를 O(1) 시간에 삭제하기는 불가능해 보인다. 왜냐하면 어떤 노드를 지우기 위해서는 이전 노드를 찾아낸 뒤 그 노드의 next 필드를 갱신하는 추가 과정이 필요하기 때문이다. 하지만 놀랍게도 삭제할 노드가 마지막 노드가 아니고 노드의 값을 쉽게 복사할 수 있다면 노드를 O(1) 시간에 삭제할 수 있다.

단순 연결리스트의 노드를 삭제하는 프로그램을 작성하라. 입력 노드는 테일 노드가 아니다.

> 힌트: 주어진 노드가 아닌 그 다음 노드를 삭제함으로써 해당 기능을 구현할 수는 없을까?

주어진 노드를 삭제하기 위해선 그 이전 노드의 next 필드를 갱신해야 한다. 보통 단순 연결리스트에서 이전 노드를 찾으려면 헤드부터 차례대로 탐색하는 과정을 거쳐야 한다. 그리고 대개 이 과정은 O(n)의 시간이 소요된다.

하지만 어떤 노드가 주어졌을 때 그 다음 노드를 삭제하는 연산은 이전 노드를 찾기 위한 탐색 과정을 생략할 수 있으므로 쉽다. 만약 다음 노드의 값을 현재 노드로 복사하고 다음 노드를 지울 수 있다면, 현재 노드를 삭제한 듯한 효과를 낼 수 있다. 시간 복잡도는 O(1)이 된다.

```java
// nodeToDelete는 마지막 노드가 아니다.
public static void deleteFromList(ListNode<Integer> nodeToDelete) {
    nodeToDelete.data = nodeToDelete.next.data;
    nodeToDelete.next = nodeToDelete.next.next;
}
```

## 7.7 리스트에서 뒤에서 k번째 원소 삭제하기
단순 연결리스트와 정수 k가 주어졌을 때 리스트의 끝에서 k번째 원소를 삭제하는 프로그램을 작성하라. 단, 리스트의 길이에 관계 없이 메모리는 상수 크기만큼만 추가로 사용할 수 있다. 리스트의 길이를 따로 저장할 수 없다고 가정한다.

> 힌트: 리스트의 전체 길이를 모른다면 작업이 쉽지 않다. 만약 리스트의 길이를 알 수 있다면, 반복자 두 개를 사용해서 끝에서 k번째 원소를 찾을 수 있겠는가?

무식한 방법으로 생각해 본다면, 먼저 단일 패스를 통해 리스트의 그 길이를 구한 뒤, 다시 리스트를 반복하면tj 삭제할 노드를 찾으면 된다. 만약 리스트가 디스크에 저장되어 있다면, 이 방법은 리스트를 두 번 탐색해야 하므로 느리다는 단점이 있다.

반복자 두 개를 사용해서 리스트를 순회해 보자. 첫 번째 반복자는 두 번째 반복자보다 k만큼 앞서게 배치하고, 함께 앞으로 나아간다. 첫 번째 반복자가 리스트의 마지막에 다다랐을 때 두 번째 반복자는 끝에서 k + 1번째 노드를 가리키게 되므로 끝에서 k번째 노드를 쉽게 삭제할 수 있다.

```java
// L에 k개 이상의 노드가 있다고 가정하고, 뒤에서 k번째 노드를 삭제한다.
public static ListNode<Integer> removeXthLast(ListNode<Integer> L, int k) {
    ListNode<Integer> dummyHead = new ListNode<>(0, L);
    ListNode<Integer> first = dummyHead.next;
    while (k-- > 0) {
        first = first.next;
    }

    ListNode<Integer> second = dummyHead;
    while (first != null) {
        second = second.next;
        first = first.next;
    }
    
    // second가 뒤에서 k + 1번째 노드를 가리키므로, 그 다음 노드를 삭제한다.
    second.next = second.next.next;
    return dummyHead.next;
}
```

리스트의 길이가 n일 때 시간 복잡도는 O(n)이고 공간 복잡도는 O(1)이 된다. 반복자 두 개를 사용한 방법과 무식한 방법을 비교해 보자. 전체 리스트는 메모리에 올릴 수 없을 만큼 크지만, k가 충분히 작아서 두 반복자 사이의 노드는 메모리에 올릴 수 있다고 가정한다. 반복자 두 개를 사용한 방법은 무식한 방법과 비교했을 때 디스크 읽는 횟수를 절반이나 줄일 수 있다.
