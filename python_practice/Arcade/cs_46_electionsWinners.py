'''
Elections are in progress!

Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.

Example

For votes = [2, 3, 5, 2] and k = 3, the output should be
solution(votes, k) = 2.

The first candidate got 2 votes. Even if all of the remaining 3 candidates vote for him, he will still have only 5 votes, i.e. the same number as the third candidate, so there will be no winner.
The second candidate can win if all the remaining candidates vote for him (3 + 3 = 6 > 5).
The third candidate can win even if none of the remaining candidates vote for him. For example, if each of the remaining voters cast their votes for each of his opponents, he will still be the winner (the votes array will thus be [3, 4, 5, 3]).
The last candidate can't win no matter what (for the same reason as the first candidate).
Thus, only 2 candidates can win (the second and the third), which is the answer.
'''

def solution(votes, k):
    # max_votes = max(votes)
    # can_win = 0
    # for v in votes:
    #     if v == max_votes and votes.count(v) == 1:
    #         can_win += 1
    #     elif v <= max_votes and v + k > max_votes:
    #         can_win += 1
    # return can_win

    m = max(votes)
    return int(votes.count(m) == 1) if k == 0 else len([n for n in votes if n + k > m])
    

print(solution(votes = [2, 3, 5, 2], k = 3)) # 2
print(solution(votes = [1, 3, 3, 1, 1], k = 0)) # 0
print(solution(votes = [5, 1, 3, 4, 1], k = 0)) # 1
print(solution(votes = [1, 1, 1, 1], k = 1)) # 4

'''
무식한 방법으로 풀이했지만 다른 사람의 풀이는 역시 멋지다.

m = max(votes)
return int(votes.count(m) == 1) if k == 0 else len([n for n in votes if n + k > m])

k가 0이면 무조건 최대 득표수의 한 명만 답이고 한 명이 아니라면 승자가 없으므로 0
k가 0이 아니면 각 투표수와 k를 더한 값이 최대 득표수보다 큰 사람이 승자가 될 수 있다.

결국 내가 푼 방식을 파이썬답게 적은 것이다.
'''