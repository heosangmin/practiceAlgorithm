'''
추석 트래픽

이번 추석에도 시스템 장애가 없는 명절을 보내고 싶은 어피치는 서버를 증설해야 할지 고민이다. 장애 대비용 서버 증설 여부를 결정하기 위해 작년 추석 기간인 9월 15일 로그 데이터를 분석한 후 초당 최대 처리량을 계산해보기로 했다. 초당 최대 처리량은 요청의 응답 완료 여부에 관계없이 임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수를 의미한다.

입력 형식
solution 함수에 전달되는 lines 배열은 N(1 ≦ N ≦ 2,000)개의 로그 문자열로 되어 있으며, 각 로그 문자열마다 요청에 대한 응답완료시간 S와 처리시간 T가 공백으로 구분되어 있다.
응답완료시간 S는 작년 추석인 2016년 9월 15일만 포함하여 고정 길이 2016-09-15 hh:mm:ss.sss 형식으로 되어 있다.
처리시간 T는 0.1s, 0.312s, 2s 와 같이 최대 소수점 셋째 자리까지 기록하며 뒤에는 초 단위를 의미하는 s로 끝난다.
예를 들어, 로그 문자열 2016-09-15 03:10:33.020 0.011s은 "2016년 9월 15일 오전 3시 10분 33.010초"부터 "2016년 9월 15일 오전 3시 10분 33.020초"까지 "0.011초" 동안 처리된 요청을 의미한다. (처리시간은 시작시간과 끝시간을 포함)
서버에는 타임아웃이 3초로 적용되어 있기 때문에 처리시간은 0.001 ≦ T ≦ 3.000이다.
lines 배열은 응답완료시간 S를 기준으로 오름차순 정렬되어 있다.

출력 형식
solution 함수에서는 로그 데이터 lines 배열에 대해 초당 최대 처리량을 리턴한다.
'''
import datetime
from typing import List
def solution(lines:List[str]) -> int:
    '''
    이게 되네???
    책의 풀이처럼 datetime 모듈을 활용했다면 좋았겠다.
    '''
    answer = 0
    logs = []
    for line in lines:
        complete_time = line.split(" ")[1].split(":")
        duration = line.split(" ")[2]
        time_to = int(complete_time[0]) * 60 * 60 * 1000 + \
                int(complete_time[1]) * 60 * 1000 + \
                int(float(complete_time[2]) * 1000)
        time_from = time_to - int(float(duration.replace("s","")) * 1000 - 1)
        logs.append([time_from, time_to])

    # 1. 로그의 시작 시각과 1초 뒤의 시각(+999) 사이에 나머지 시각들이 포함
    # 2. 로그의 완료 시각과 1초 뒤의 시각(+999) 사이에 나머지 시각들이 포함
    # 3. 로그의 시작 시각이 나머지 로그의 실행 시간에 포함
    for i in range(len(logs)):
        for j in range(2):
            local_max = 1
            for k in range(len(logs)):
                if i != k:
                    if logs[i][j] <= logs[k][0] <= logs[i][j] + 999 or \
                        logs[i][j] <= logs[k][1] <= logs[i][j] + 999 or \
                        logs[k][0] <= logs[i][j] <= logs[k][1]:
                        local_max += 1
                answer = max(answer, local_max)

    return answer

def solution_book(lines:List[str]) -> int:
    combined_logs = []
    for log in lines:
        logs = log.split(" ")
        timestamp = datetime.datetime.strptime(logs[0] + " " + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        combined_logs.append((timestamp, -1))
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))

    accumulated = 0
    max_requests = 1
    combined_logs.sort(key=lambda x: x[0])
    for i, elem1 in enumerate(combined_logs):
        current = accumulated

        # 1초 미만 윈도우 범위 요청 수 계산
        for elem2 in combined_logs[i:]:
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:
                current += elem2[1]
        max_requests = max(max_requests, current)
        accumulated += elem1[1]
    
    return max_requests

inp = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
] # 1
#print(solution(inp))
print(solution_book(inp))

inp = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
] # 2
#print(solution(inp))
print(solution_book(inp))

inp = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
] # 7
#print(solution(inp))
print(solution_book(inp))

