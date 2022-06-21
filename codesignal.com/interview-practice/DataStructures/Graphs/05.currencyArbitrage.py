'''
2022/06/21

Note: Try to solve this task in O(n3) time, where n is a number of currencies, since this is what you'll be asked to do during an interview.

A currency converter has the exchange rates exchange, such that exchange[i][j] represents the amount of money you would get for exchanging 1 unit of the ith currency for 1 unit of the jth currency. A "non-exchange" (that is, exchanging a currency with itself) is represented by exchange[i][i] = 1.

Write a function that returns True if it's possible to make money by doing a series of exchanges (i.e. to start with some currency C and to end with a greater amount of currency C after a series of exchanges), and False otherwise.

Example

For exchange = [[1, 0.5, 0.2], [1.8, 1, 0.5], [3.95, 1.2, 1]], the output should be
solution(exchange) = false.
There is no way of transferring money through a series of exchanges to make more money. For example, taking $1 from currency 0, we can get $0.50 (currency 1), then get $0.25 (currency 2) and finally $0.9875 (currency 0). This is an example of one series of exchanges; there is no possible series of exchanges that makes money.

For exchange = [[1, 0.5, 0.2], [1.8, 1, 0.5], [4.05, 1.2, 1]], the output should be
solution(exchange) = true.
Taking $1 from currency 0, we can get $0.50 (currency 1), then get $0.25 (currency 2), and finally get $1.0125 (currency 0).

For exchange = [[1, 0.5, 0.2], [2.05, 1, 0.5], [3.3, 1.2, 1]], the output should be
solution(exchange) = true.
Taking $1 from currency 0, we can get $0.50 (currency 1), and then get $1.025 (currency 0).

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.float exchange

exchange[i][j] represents the amount of money you would get for exchanging 1 unit of the ith currency for 1 unit of the jth currency.

Guaranteed constraints:
 1 ≤ exchange.length ≤ 14,
exchange[i].length = exchange.length,
0.001 ≤ exchange[i][j] ≤ 1000,
exchange[i][i] = 1.

[output] boolean

Return True if it's possible to make money by doing a series of currency exchanges, and False otherwise.
'''
# 플로이드 워셜 알고리즘을 활용할 수 있다.
def solution(exchange):
    n = len(exchange)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                exchange[i][j] = max(exchange[i][j], exchange[i][k] * exchange[k][j])
    for x in range(n):
        if exchange[x][x] > 1:
            return True
    return False


exchange = [[1, 0.5, 0.2], [1.8, 1, 0.5], [3.95, 1.2, 1]]
print(solution(exchange))

exchange = [[1, 0.5, 0.2], [1.8, 1, 0.5], [4.05, 1.2, 1]]
print(solution(exchange))

exchange = [[1, 0.5, 0.2], [2.05, 1, 0.5], [3.3, 1.2, 1]]
print(solution(exchange))