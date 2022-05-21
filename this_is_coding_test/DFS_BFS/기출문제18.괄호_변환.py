'''
2022/05/21

https://programmers.co.kr/learn/courses/30/lessons/60058

'''

def is_valid(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return True

def is_balanced(s):
    if len(s) % 2 != 0:
        return False
    if s.count("(") != s.count(")"):
        return False
    return True

def solution(w):
    if w == "":
        return ""

    u = ""
    v = ""
    for i in range(len(w)):
        u += w[i]
        if is_balanced(u):
            v = w[i+1:]
            break
    #print("u:",u,", v:", v)
    if is_valid(u):
        return u + solution(v)
    else:
        tmp = list(u[1:-1])
        for i in range(len(tmp)):
            if tmp[i] == "(":
                tmp[i] = ")"
            else:
                tmp[i] = "("
        
        return "(" + solution(v) + ")" + "".join(tmp)


print(solution("()))((()"))
#print(solution("()))((()((())())"))