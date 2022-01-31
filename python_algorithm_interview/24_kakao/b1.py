from typing import List
def solution_my(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    result = []
    for i in range(n):
        ans = bin(arr1[i] | arr2[i])[2:].zfill(n)
        ans = ans.replace("1", "#").replace("0", " ")
        result.append(ans)
        
    return result

def solution_book(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    maps = []
    for i in range(n):
        maps.append(
            bin(arr1[i] | arr2[i])[2:]
                .zfill(n)
                .replace("1", "#")
                .replace("0", " ")
        )
    return maps

n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
print(solution_my(n, arr1, arr2))
print(solution_book(n, arr1, arr2))

n = 6
arr1 = [46,33,33,22,31,50]
arr2 = [27,56,19,14,14,10]
print(solution_my(n, arr1, arr2))
print(solution_book(n, arr1, arr2))