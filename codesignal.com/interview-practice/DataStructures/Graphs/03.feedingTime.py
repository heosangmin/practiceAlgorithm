'''
2022/06/15

https://app.codesignal.com/interview-practice/task/bdatSZvuKFyjJ8eYw

You are the head zookeeper at a large zoo. You've been contacted by schools in the area that want to bring in classes so that students can feed the animals. The animals can only be fed once a day, so no two classes can come on the same day if they want to feed the same animals.

You have a list classes, such that classes[i] is a list of animals that the ith class wants to feed. Classes i and j cannot come on the same day if an animal in classes[i] also appears in classes[j] (for i ≠ j). Your job is to determine the minimum number of days you would need to have all the classes come to feed the animals if they can all come within 5 days. If it isn't possible for all the classes to come within 5 days, return -1 instead.

Example

For classes = [["Tiger", "Lima", "Frog"], ["Tiger", "Zebra","Lion"], ["Tiger", "Rabbit"], ["Emu", "Zebra", "Rabbit"]], the output should be
solution(classes) = 3.
Classes 0, 1, and 2 all want to feed the Tiger, so they have to come on different days. Class 3 cannot come on the same day as class 1 (because of the Zebra) or class 2 (because of the Rabbit), but they can come on the same day as class 0. Therefore it only takes 3 days for all the classes to visit the zoo.

For classes = [["Tiger", "Lima", "Frog"], ["Tiger", "Zebra", "Lion"], ["Tiger", "Rabbit"], ["Lima", "Zebra", "Rabbit"]], the output should be
solution(classes) = 4.
Each class has to come on a separate day, because every pair of classes has at least one animal in common.

For classes = [["Lion", "Emu"], ["Giraffe", "Peacock"], ["Lima"], ["Tiger", "Cheetah", "Slugs"], ["Snakes", "Sealion"]], the output should be
solution(classes) = 1.
No classes have animals in common, so they can all come on the same day.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.string classes

classes[i] is a list of animals that the ith class wants to feed.

Guaranteed constraints:
1 ≤ classes.length ≤ 15,
1 ≤ classes[i].length ≤ 10,
1 ≤ classes[i][j].length ≤ 14.

[output] integer

The minimum number of days you would need to have all the classes come to feed the animals. If it isn't possible for all the classes to come within 5 days, return -1 instead.
'''

# kien_the_sun's solution
def solution(c):
    def dfs(curr,dp):
        if curr == len(c): # 모든 학급이 참여 가능
            return True
        for i,v in enumerate(dp):
            if not (c[curr] & v): # 이미 먹이를 준 동물들과의 교집합이 없을 경우
                dp[i] |= c[curr]
                if dfs(curr+1,dp):
                    return True
                dp[i] -= c[curr]
        return False
    c=[set(x) for x in c] # 각 학급의 동물 리스트를 셋으로 변경
    for i in range(1,6): # 1일부터 5일까지
        dp = [set() for _ in range(i)] 
        if dfs(0,dp):
            return i 
    return -1 # 5일 넘어가면 -1
    

classes = [["Tiger", "Lima", "Frog"], ["Tiger", "Zebra","Lion"], ["Tiger", "Rabbit"], ["Emu", "Zebra", "Rabbit"]]
print(solution(classes)) # 3
classes = [["Tiger", "Lima", "Frog"], ["Tiger", "Zebra", "Lion"], ["Tiger", "Rabbit"], ["Lima", "Zebra", "Rabbit"]]
print(solution(classes)) # 4
classes = [["Lion", "Emu"], ["Giraffe", "Peacock"], ["Lima"], ["Tiger", "Cheetah", "Slugs"], ["Snakes", "Sealion"]]
print(solution(classes)) # 1