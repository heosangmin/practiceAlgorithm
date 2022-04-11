def solution(sequence):
    decreased = 0
    increasedIndex = 0
    for i in range(1, len(sequence)):
        if sequence[increasedIndex] >= sequence[i]:
            decreased += 1
            if increasedIndex == 0:
                increasedIndex = 1
        else:
            increasedIndex = i

        print("increasedIndex: ", increasedIndex)    
        
        if decreased > 1:
            return False
    return True


print(solution([1, 2, 5, 3, 5]))

