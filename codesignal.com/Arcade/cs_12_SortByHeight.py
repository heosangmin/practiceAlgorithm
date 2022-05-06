'''
Some people are standing in a row in a park.
There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
People can be very tall!

For a = [-1, 150, 190, 170, -1, -1, 160, 180],
the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''
def solution(a):
    b = [e for e in a if e > 0]
    b.sort()
    for i in range(len(a)):
        if a[i] > 0:
            a[i] = b.pop(0)
    return a

a = [-1, 150, 190, 170, -1, -1, 160, 180]

print(solution(a))