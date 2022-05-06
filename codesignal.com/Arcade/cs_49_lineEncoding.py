'''
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
solution(s) = "2a3bc".
'''

def solution(s):
    result = ""
    count = 1
    for i in range(1, len(s)+1):
        if i == len(s) or s[i] != s[i-1]:
            result = result + s[i-1] if count <= 1 else result + str(count) + s[i-1]
            count = 1
        else:
            count += 1
    return result


print(solution("aabbbc")) # 2a3bc
print(solution("abbcabb")) # a2bca2b
print(solution("abcd")) # abcd
print(solution("wwwwwwwawwwwwww")) # 7wa7w

'''
반복문의 인덱스를 헷갈리기 좋은 문제다.
조건문의 조건을 배치하는 순서에 따라서도 처리가 달라진다.

자바에서 다음과 같이 연습해 본 적이 있어서 참고가 되었다.

public static String encoding(String s) {
    int count = 1;
    StringBuilder ss = new StringBuilder();
    for (int i = 1; i < s.length(); i++) {
        if (i == s.length() || s.charAt(i) != s.charAt(i - 1)) {
            ss.append(count);
            ss.append(s.charAt(i - 1));
            count = 1;
        } else {
            count++;
        }
    }
    return ss.toString();
}
'''