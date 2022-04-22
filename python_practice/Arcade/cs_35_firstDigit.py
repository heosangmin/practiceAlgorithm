'''
Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
solution(inputString) = '1';
For inputString = "q2q-q", the output should be
solution(inputString) = '2';
For inputString = "0ss", the output should be
solution(inputString) = '0'.
'''

def solution(inputString):
    for x in inputString:
        if x.isdigit():
            return x

inputString = "var_1__Int"
print(solution(inputString))
inputString = "q2q-q"
print(solution(inputString))
inputString = "0ss"
print(solution(inputString))

'''
난이도 배치가 이상하다.
엄청 쉽다가 갑자기 어렵다가 한다.

다른 사람 자바 풀인데 재미있다.
char solution(String inputString) {
    return inputString.replaceAll("[^0-9]","").charAt(0);
}

'''