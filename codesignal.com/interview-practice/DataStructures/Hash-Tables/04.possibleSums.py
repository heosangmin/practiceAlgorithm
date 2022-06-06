'''
2022/06/06

https://app.codesignal.com/interview-practice/task/rMe9ypPJkXgk3MHhZ

You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.

Example

For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
solution(coins, quantity) = 9.

Here are all the possible sums:

50 = 50;
10 + 50 = 60;
50 + 100 = 150;
10 + 50 + 100 = 160;
50 + 50 = 100;
10 + 50 + 50 = 110;
50 + 50 + 100 = 200;
10 + 50 + 50 + 100 = 210;
10 = 10;
100 = 100;
10 + 100 = 110.
As you can see, there are 9 distinct sums that can be created from non-empty groupings of your coins.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer coins

An array containing the values of the coins in your collection.

Guaranteed constraints:
1 ≤ coins.length ≤ 20,
1 ≤ coins[i] ≤ 104.

[input] array.integer quantity

An array containing the quantity of each type of coin in your collection. quantity[i] indicates the number of coins that have a value of coins[i].

Guaranteed constraints:
quantity.length = coins.length,
1 ≤ quantity[i] ≤ 105,
(quantity[0] + 1) * (quantity[1] + 1) * ... * (quantity[quantity.length - 1] + 1) <= 106.

[output] integer

The number of different possible sums that can be created from non-empty groupings of your coins.
'''
# from itertools import combinations
# def solution(coins, quantity):
#     all_coins = []
#     for i in range(len(coins)):
#         all_coins += [coins[i]] * quantity[i]
#     s = set()
#     for i in range(1, len(all_coins)+1):
#         for x in list(map(sum,(combinations(all_coins, i)))):
#             s.add(x)
#     return len(s)

# 동전들의 조합으로 풀려고 했더니 테스트 케이스의 quantity가 많아 시간을 초과한다.
# 해시 테이블 문제이고 모든 경우의 수를 고려해야 한다는 것은 그리디나 동적 계획법으로 풀어야 하나?

def solution(coins, quantity):
    possible_sums = {0}
    for c, q in zip(coins, quantity):
        possible_sums = {x + c * i for x in possible_sums for i in range(q + 1)}
    return len(possible_sums) - 1

print(solution(coins = [10, 50, 100], quantity = [1, 2, 1])) # 9
print(solution(coins = [1, 2], quantity = [50000, 2])) # 50004