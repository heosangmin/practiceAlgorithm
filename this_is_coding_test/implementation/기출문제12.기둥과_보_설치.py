'''
2022/05/18


'''

def check(answer):
    for x, y, a in answer:
        if a == 0: # 기둥
            # 바닥 위, 보의 한쪽 끝 위, 다른 기둥 위
            if y == 0 or \
                [x-1, y, 1] in answer or \
                [x, y, 1] in answer or \
                [x, y-1, 0] in answer:
                continue
            return False
        else: # 보
            # 한쪽 끝 부분이 기둥 위, 양쪽 끝 부분이 다른 보와 동시에 연결
            if [x, y-1, 0] in answer or \
                [x+1, y-1, 0] in answer or \
                ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []

    for x,y,a,b in build_frame:
        if b == 0: # 삭제
            answer.remove([x, y, a]) # 일단 삭제
            if not check(answer): # 전체 검사 해보고
                answer.append([x, y, a]) # 삭제해서는 안 되면 다시 설치
        else: # 설치
            answer.append([x, y, a]) # 일단 설치
            if not check(answer): # 전체 검사 해보고
                answer.remove([x, y, a]) # 안 되면 삭제

    return sorted(answer)

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
correct = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
answer = solution(n, build_frame)
print(correct == answer, answer)

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
correct = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
answer = solution(n, build_frame)
print(correct == answer, answer)