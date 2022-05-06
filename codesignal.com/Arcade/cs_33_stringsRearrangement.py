'''
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
solution(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
solution(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.
'''
def solution(inputArray):
    result = []
    prev_elements = []

    def dfs(nums):
        if not nums:
            result.append(prev_elements[:])
            return

        for i in nums:
            new_nums = nums.copy()
            new_nums.remove(i)
            prev_elements.append(i)
            dfs(new_nums)
            prev_elements.pop()

    dfs(inputArray)
    # print(result)

    for strings in result:
        diffList = []
        for i in range(0, len(strings)-1):
            diffCount = 0
            for j in range(0, len(strings[i])):
                if strings[i][j] != strings[i+1][j]:
                    diffCount += 1
            diffList.append(diffCount)
        
        # print(diffList, [1]*(len(strings)-1))
        if diffList == [1]*(len(strings)-1):
            return True

    return False


print(solution(["aba", "bbb", "bab"])) # False
print(solution(["ab", "bb", "aa"])) # True
