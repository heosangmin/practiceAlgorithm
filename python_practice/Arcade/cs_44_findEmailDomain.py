'''
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.

Example

For address = "prettyandsimple@example.com", the output should be
solution(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should be
solution(address) = "codesignal.com".
'''
import re
def solution(address):
    #return re.findall("(?<=@)[^@]+$", address)[0]
    #return address[address.rfind("@")+1:]
    return address.split("@")[-1]
    

print(solution(address = "prettyandsimple@example.com"))
print(solution(address = "fully-qualified-domain@codesignal.com"))
print(solution(address = "\"very.unusual.@.unusual.com\"@usual.com"))

'''
이건 또 무슨 함정이지??
유효한 이메일 주소인지 체크하는 것도 아니고 도메인 파트를 반환하면 된다고??

역시나 테스트 케이스에 @이 두 번 이상 등장하는 경우가 있다.
자바의 lastIndexOf()가 있다면 더 수월하겠지만 파이썬에서는 어떻게 해야할까?
정규표현식으로?

다른 사람들의 풀이를 보니
1. return address[address.rfind("@")+1:]
문자열의 rfind라는 함수를 바로 쓸 수도 있고
2. return address.split("@")[-1]
split으로 나눠서 마지막 요소를 반환하는 것도 가능.
'''