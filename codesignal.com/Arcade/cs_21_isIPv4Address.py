'''
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.
'''

# def solution(inputString):
#     l = inputString.split(".")
#     if len(l) != 4:
#         return False
#     for x in l:
#         if len(x) > 1 and x.startswith("0"):
#             return False
#         if not x.isdecimal():
#             return False
#         if int(x) < 0:
#             return False
#         if int(x) > 255:
#             return False
#     return True

# 다른 사람의 풀이
# all() 존재를 알고 있었던가
# 하지만 테스트 케이스가 갱신된 이유인지 이 코드는 에러임
# 00.123.123.123의 경우 isdigit()가 00을 True로 인식하므로
def solution(inputString):
    l = inputString.split(".")
    return len(l) == 4 and all(x.isdigit() and 0 <= int(x) <= 255 for x in l)

print(solution("172.16.254.1")) # True
print(solution("172.316.254.1")) # False
print(solution(".254.255.0")) # False
print(solution(".254.255.00")) # False

# 자체 모듈을 쓰는 방법도 있음
# import ipaddress
# def solution(inputString):
#     try:
#         ipaddress.ip_address(inputString)
#     except:
#         return False
#     return True