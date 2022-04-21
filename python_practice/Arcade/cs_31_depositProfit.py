'''
You have deposited a specific amount of money into your bank account. Each year your balance increases at the same growth rate. With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.

Example

For deposit = 100, rate = 20, and threshold = 170, the output should be
solution(deposit, rate, threshold) = 3.

Each year the amount of money in your account increases by 20%. So throughout the years, your balance would be:

year 0: 100;
year 1: 120;
year 2: 144;
year 3: 172.8.
Thus, it will take 3 years for your balance to pass the threshold, so the answer is 3.
'''

def solution(deposit, rate, threshold):
    years = 0
    while deposit < threshold:
        deposit += deposit * (rate / 100)
        years +=1
    return years


print(solution(100, 20, 170)) # 3

# 다른 사람의 풀이인데 로그 함수가 뭔지 제대로 공부하지 않으면 안 되겠다.
# return math.ceil(math.log(threshold/deposit, 1+rate/100))