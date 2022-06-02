'''
투 포인터(Two Pointer) 알고리즘은 '리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리'하는 알고리즘을 의미한다. 예를 들어 한 반에 학생이 40명이 있을 때, 모든 학생을 번호 순서대로 일렬로 세운 뒤, 학생들을 순차적으로 지목해야할 경우를 생각해 보자. 2,3,4,5,6,7번 학생을 지목해야 할 때, 우리는 번호로 한명씩 부르기보다는 '2번부터 7번까지의 학생'이라고 부를 수도 있다. 이처럼 리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 '시작점'과 '끝점' 2개의 점으로 접근할 데이터의 범위를 표현할 수 있다.

이러한 투 포인터 알고리즘을 이용하여 '특정한 합을 가지는 부분 연속 수열 찾기' 문제를 풀어보자. '특정한 합을 가지는 부분 연속 수열 찾기 문제'는 양의 정수로만 구성된 리스트가 주어졌을 때, 그 부분 연속 수열 중에서 '특정한 합'을 갖는 수열의 개수를 출력하는 문제이다. 예를 들어 다음과 같이 1,2,3,2,5를 차례대로 원소로 갖는 리스트가 주어졌다고 해보자.

1, 2, 3, 2, 5

이때 합계 값을 5라고 설정하면 다음과 같은 3가지 경우의 수만 존재한다.

1, "2", "3", 2, 5
1, 2, "3", "2", 5
1, 2, 3, 2, "5"

그러면 이 문제를 투 포인터 알고리즘을 이용하여 풀어보자. 투 포인터 알고리즘의 특징은 2개의 변수를 이용해 리스트 상의 위치를 기록한다는 점이다. '특정한 합을 가지는 부분 연속 수열 찾기' 문제에서는 부분 연속 수열의 시작점(start)과 끝점(end)의 위치를 기록한다. 특정한 부분합을 M이라고 할 때, 구체적인 알고리즘은 다음과 같다.

1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)을 가리키도록 한다.
2. 현재 부분합이 M과 같다면 카운트한다.
3. 현재 부분합이 M보다 작으면 end를 1 증가시킨다.
4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가시킨다.
5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다.

투포인터 알고리즘은 구현 가능한 방식이 매우 많다는 특징이 있다. 여기서는 시작점을 반복문을 이용하여 증가시키며, 증가할 때마다 끝점을 그것에 맞게 증가시키는 방식으로 구현하였다. 이 문제를 투 포인터 알고리즘으로 해결할 수 있는 이유는 기본적으로 시작점을 오른쪽으로 이동시키면 항상 합이 감소하고, 끝점을 오른쪽으로 이동시키면 항상 합이 증가하기 때문이다. 만약에 리스트 내 원소에 음수 테이터가 포함되어 있는 경우에는 투 포인터 알고리즘으로 문제를 해결할 수 없다.
'''

n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
        
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)