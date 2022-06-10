'''
2022/06/10

https://app.codesignal.com/interview-practice/task/aRwxhGcmvhf6vKPCp

Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....

Here is some info on Unix file system paths:

/ is the root directory; the path should always start with it even if it isn't there in the given path;
/ is also used as a directory separator; for example, /code/fights denotes a fights subfolder in the code folder in the root directory;
this also means that // stands for "change the current directory to the current directory"
. is used to mark the current directory;
.. is used to mark the parent directory; if the current directory is root already, .. does nothing.
Example

For path = "/home/a/./x/../b//c/", the output should be
solution(path) = "/home/a/b/c".

Here is how this path was simplified:
* /./ means "move to the current directory" and can be replaced with a single /;
* /x/../ means "move into directory x and then return back to the parent directory", so it can replaced with a single /;
* // means "move to the current directory" and can be replaced with a single /.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string path

A line containing a path presented in Unix style format. All directories in the path are guaranteed to consist only of English letters.

Guaranteed constraints:
1 ≤ path.length ≤ 5 · 104.

[output] string

The simplified path.
'''

# 디렉토리 패스 문제이므로 대놓고 스택을 쓰라는 소리로 들린다.

def solution(path):
    stack = []
    for p in path.split("/"):
        if p == '..':
            if len(stack) > 0:
                stack.pop()
        elif p == '.' or p == '':
            continue
        else:
            stack.append(p)
    return "/" + "/".join(stack)

print(solution(path = "/home/a/./x/../b//c/")) # "/home/a/b/c"
print(solution(path = "/../")) # "/"
print(solution(path = "a/../../b/")) # "/b"