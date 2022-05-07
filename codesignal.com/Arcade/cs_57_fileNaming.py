'''
2022/05/07

You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
solution(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

'''

def solution(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j = 1
            while names[i] + "(" + str(j) + ")" in names[:i]:
                j += 1
            names[i] += "(" + str(j) + ")"
    return names

    # m = {}
    # r = []
    # for name in names:
    #     if name not in m:
    #         m[name] = 1
        
    #     if r.count(name) == 0:
    #         r.append(name)
    #         continue

    #     while r.count(name + "(" + str(m[name]) + ")") > 0:
    #         m[name] += 1
        
    #     r.append(name + "(" + str(m[name]) + ")")

    # return r

'''
쉬운듯 아닌듯한 문제로 한 시간을 넘게 소비했다.
다른 사람 풀이를 보니 나는 도대체 뭘 한 건가 싶다.
'''


print(solution(names = ["doc", "doc", "image", "doc(1)", "doc"]))

print(solution(names = ["a(1)","a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]))
'''
["a(1)", 
"a(6)", 
"a", 
"a(2)", 
"a(3)", 
"a(4)", 
"a(5)", 
"a(7)", 
"a(8)", 
"a(9)", 
"a(10)", 
"a(11)"]
'''

print(solution(names = ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]))
'''
 ["dd", 
 "dd(1)", 
 "dd(2)", 
 "dd(3)", 
 "dd(1)(1)", 
 "dd(1)(2)", 
 "dd(1)(1)(1)", 
 "dd(4)", 
 "dd(1)(3)"]
'''
