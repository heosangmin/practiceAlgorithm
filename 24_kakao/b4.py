'''
셔틀버스

카카오에서는 무료 셔틀버스를 운행하기 때문에 판교역에서 편하게 사무실로 올 수 있다. 카카오의 직원은 서로를 '크루'라고 부르는데, 아침마다 많은 크루들이 이 셔틀을 이용하여 출근한다.

이 문제에서는 편의를 위해 셔틀은 다음과 같은 규칙으로 운행한다고 가정하자.

셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다. 예를 들어 09:00에 도착한 셔틀은 자리가 있다면 09:00에 줄을 선 크루도 탈 수 있다.
일찍 나와서 셔틀을 기다리는 것이 귀찮았던 콘은, 일주일간의 집요한 관찰 끝에 어떤 크루가 몇 시에 셔틀 대기열에 도착하는지 알아냈다. 콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하여라.

단, 콘은 게으르기 때문에 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다. 또한, 모든 크루는 잠을 자야 하므로 23:59에 집에 돌아간다. 따라서 어떤 크루도 다음날 셔틀을 타는 일은 없다.

입력 형식
셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m, 크루가 대기열에 도착하는 시각을 모은 배열 timetable이 입력으로 주어진다.

0 ＜ n ≦ 10
0 ＜ t ≦ 60
0 ＜ m ≦ 45

timetable은 최소 길이 1이고 최대 길이 2000인 배열로, 하루 동안 크루가 대기열에 도착하는 시각이 HH:MM 형식으로 이루어져 있다.
크루의 도착 시각 HH:MM은 00:01에서 23:59 사이이다.

출력 형식
콘이 무사히 셔틀을 타고 사무실로 갈 수 있는 제일 늦은 도착 시각을 출력한다. 도착 시각은 HH:MM 형식이며, 00:00에서 23:59 사이의 값이 될 수 있다.
'''
from typing import List
import collections

def solution(n, t, m, timetable:List[str]):
    
    def hhmm_to_m(hhmm:str) -> int:
        hhmm_lst = hhmm.split(":")
        return int(hhmm_lst[0]) * 60 + int(hhmm_lst[1])

    def m_to_hhmm(minutes:int) -> str:
        h, m = divmod(minutes, 60)
        return str(h).zfill(2) + ":" + str(m).zfill(2)

    answer = ''
    q = []
    for time in timetable:
        q.append(hhmm_to_m(time))
    
    q.sort()
    start_time = 540
    the_last_time = start_time + (t * (n - 1))

    for i in range(0, n): # 시간대로 진행하며 대기열을 줄여 나간다
        now = start_time + i * t
        if now == the_last_time:
            if len(q) < m: # 1. 마지막 버스 + 자리 남음 -> 마지막 시간
                answer = now
            elif q[0] > the_last_time: # 2. 마지막 버스 + 자리 없음 + 마지막 시간 전에 온 사람이 없다 -> 마지막 시간
                answer = now
            else: # 3. 마지막 버스 + 자리 없음 + 마지막 시간 전에 온 사람이 있다 -> m번째 사람보다 -1분??
                answer = q[m - 1] - 1
        else:
            for _ in range(m):
                if q and q[0] <= now:
                    q.pop(0)
                else:
                    break

    return m_to_hhmm(answer)

def solution_book(n, t, m, timetable:List[str]):
    # n번의 버스, m명의 대기열이므로 n * m번 반복한다.
    #     대기열이 남아 있고 대기열 맨 앞의 사람(timetable[0])이 현재 시간보다 먼저 왔을 경우
    #         버스에 태우고(pop) 그보다 1분 빠른 시간을 정답 후보로 한다.
    #     아닐 경우(버스에 자리는 있는데 대기열이 없거나 이번 버스를 못 타는 사람들일 경우)
    #         해당 시간을 정답 후보로 한다.
    # 
    # 그리고, 리스트 컴프리헨션을 사용하는 경험을 늘리자.

    # 입력값 전처리
    timetable = [
        int(time[:2]) * 60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()

    current = 540
    for _ in range(n):
        for _ in range(m):
            # 대기가 있는 경우 1분전 도착
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0) - 1
            else: # 대기가 없는 경우 정시 도착
                candidate = current
        candidate += t
    
    # 시간값 재변환
    h, m = divmod(candidate, 60)
    return str(h).zfill(2) + ":" + str(m).zfill(2)

n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(1, solution(n, t, m, timetable)) # "09:00"
# print(1, solution_book(n, t, m, timetable)) # "09:00"

n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
print(2, solution(n, t, m, timetable)) # "09:09"
# print(2, solution_book(n, t, m, timetable)) # "09:09"

n = 2
t = 1
m = 2
timetable = ["09:00", "09:00", "09:00", "09:00"]
print(3, solution(n, t, m, timetable)) # "08:59"
# print(3, solution_book(n, t, m, timetable)) # "08:59"

n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(4, solution(n, t, m, timetable)) # "00:00"
# print(4, solution_book(n, t, m, timetable)) # "00:00"

n = 1
t = 1
m = 1
timetable = ["23:59"]
print(5, solution(n, t, m, timetable)) # "09:00"
# print(5, solution_book(n, t, m, timetable)) # "09:00"

n = 10
t = 60
m = 45
timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
print(6, solution(n, t, m, timetable)) # "18:00"
# print(6, solution_book(n, t, m, timetable)) # "18:00"
