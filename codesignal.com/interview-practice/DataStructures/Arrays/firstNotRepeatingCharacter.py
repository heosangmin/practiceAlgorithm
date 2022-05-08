'''
2022/05/08

Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
solution(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
solution(s) = '_'.

There are no characters in this string that do not repeat.
'''

def solution(s):
    # m = {}
    # for c in s:
    #     if c not in m:
    #         m[c] = 0
    #     m[c] += 1
    # for k in m.keys():
    #     if m[k] == 1:
    #         return k
    # return "_"

    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return "_"

'''
리스트의 자료구조에 대해 자세히 공부할 필요가 있다.
매번 멋지다싶은 해법은 포인터를 두 개 쓰는 경우가 많은 것 같다.

자바의 경우

char solution(s) {
    char[] c = s.toCharArray();
    for (int i = 0; i < s.length(); i++) {
        if ( s.indexOf(c[i]) == s.lastIndexOf(c[i]) ) {
            return c[i];
        }
    }
    return "_";
}
'''

print(solution("abacabad")) # c