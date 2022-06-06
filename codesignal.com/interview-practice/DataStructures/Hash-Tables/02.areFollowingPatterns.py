'''
2022/06/06

https://app.codesignal.com/interview-practice/task/3PcnSKuRkqzp8F6BN

Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
solution(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
solution(strings, patterns) = false.
'''

# def solution(strings, patterns):
    # m = {}
    # for i in range(len(strings)):
    #     if patterns[i] not in m:
    #         if strings[i] in m.values():
    #             return False
    #         m[patterns[i]] = strings[i]
    #     else:
    #         if m[patterns[i]] != strings[i]:
    #             return False
    # return True

def solution(strings, patterns):
    return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))


strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]
print(solution(strings, patterns))


strings = ["cat", "dog", "doggy"]
patterns = ["a", "b", "b"]
print(solution(strings, patterns))

strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "c"]
print(solution(strings, patterns)) # False