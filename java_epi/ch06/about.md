# 6. 문자열
문자열이 메모리에서 어떻게 표현되는지 알아야 한다. 그리고 기본적인 문자열 연산(비교, 복사, 조인, 분할, 매칭 등)에 대한 이해도 필요하다. 이 장에서는 문자열과 관련된 문제를 다루는데, 기본적인 기능을 이용하면 대부분 풀 수 있다. 고급 문자열 알고리즘은 해시 테이블(12장)이나 동적 프로그래밍(16장)을 추가적으로 사용하기도 한다.

## 문자열 부트캠프
회문(palindrome)은 거꾸로 읽어도 같은 문자열을 뜻한다. 다음 프로그램은 주어진 문자열이 회문인지 확인한다. 입력 문자열을 뒤집어 추가 공간을 사용하기보단, 입력 문자열을 앞뒤로 동시에 읽어서 공간을 절약한다. 문자열의 길이가 짝수이든 홀수이든 동일하게 처리할 수 있다는 사실에 주목하라.

```java
public static boolean isPalindrome(String s) {
    for (int i = 0, j = s.length() - 1; i < j; ++i, --j) {
        if (s.charAt(i) != s.charAt(j)) {
            return false;
        }
    }
    return true;
}
```
n이 문자열의 길이라고 할 때, 시간 복잡도는 O(n)이고 공간 복잡도는 O(1)이다.

## 문자열 문제를 풀기 전에 알고 있어야 할 내용
- 배열과 비슷하게 문자열 문제도 O(n) 공간을 사용하면 무식하지만 간단한 해법이 존재한다. O(1)의 공간 복잡도를 사용하는 해법으로 개선할 수 있다.(문제 6.6, 6.4)
- 문자열은 암묵적으로 불변(immutable)이라는 사실을 명심하라. 따라서 문자열을 이어 붙이려면 새로운 문자열을 추가로 할당해야 한다. Java에서 문자 배열 혹은 StringBuilder가 불변하는 문자열을 대체한다.(문제 6.6)
- 가변 문자열을 앞에서부터 갱신해 나가는 방법은 느리다. 따라서 가능하면 값을 뒤에서부터 쓰는 것이 좋다.(문제 6.4)

## 문자열 라이브러리 이해하기
Java 문자열을 잘 조작하기 위해서는 String 클래스와 StringBuilder 클래스에 익숙해질 필요가 있다. Java의 문자열은 불변(immutable)이기 때문에 StringBuilder가 필요하다. 따라서 문자열을 효율적으로 만들기 위해선 가변(mutable) 문자열 클래스가 필요하다.

다음은 문자열의 핵심 메서드 몇 가지이다.
- `charAt(1)`
- `compareTo("foo")`
- `concat("bar")`: 기존 문자열을 갱신하지 않고, 새로운 문자열을 반환한다.
- `contains("aba")`
- `endsWith("YZ")`
- `indexOf("needle")`
- `indexOf("needle", 12)`
- `indexOf('A')`
- `indexOff('B', offset)`
- `lastIndexOf("needle")`
- `length()`
- `replace('a','A')`
- `replace("a","ABC")`
- `"foo::bar::abc".split("::")`
- `startsWith(prefix)`
- `startsWith("www", "http://".length())`
- `substring(1)`
- `substring(1,5)`
- `toCharArray()`
- `toLowerCase()`
- `trim()`.

substring() 메서드는 특히 중요한데, 두 가지 다른 용례 때문에 잘못 사용하기 쉽다. 하나는 시작 인덱스가 주어졌을 때 접미사(접두사랑 헷갈리기 쉽다)를 반환하는 경우고, 다른 하나는 시작 인덱스와 마지막 인덱스가 함께 주어지는 경우다(이 경우에 시작 인덱스의 문자를 포함하는데 반해 마지막 인덱스의 문자는 포함하지 않는다).

다음은 StringBuilder의 핵심 메서드 몇 가지이다.
- `append()`
- `charAt()`
- `delete()`
- `deleteCharAt()`
- `insert()`
- `replace()`
- `toString()`

## 6.1 문자열과 정수 상호 전환하기
정수형 숫자(음의 정수를 포함)값이 문자열로 주어졌을 때, 이를 정수형 숫자로 바꾸는 프로그램을 작성하라. 정수형 숫자가 입력으로 주어진다면 반대로 문자열을 출력한다. 이때 Java의 parseInt와 같은 라이브러리 함수를 사용하면 안 된다.

> 힌트: 숫자를 차례대로 만들어보자.

정수를 문자열로 바꾸는 문제를 먼저 생각해보자. 우선 0과 9 사이에 있는 한 자리 숫자는 문자 한 개로 표현이 가능하므로 쉽게 바꿀 수 있다. 즉, 이 경우에는 숫자를 문자 하나로 이루어진 문자열로 표현한다.

만약 자릿수가 하나 이상이라면, 자연스럽게 각 자리에 위치한 숫자를 하나씩 바꿔주면 된다. 여기서 핵심은 어떤 양의 정수 x의 최하위 숫자는 x mod 10으로 표현되고, 나머지 숫자는 x/10으로 표현된다는 점이다. 이 방법은 자릿수를 역순으로 배열한다. 예를 들어 423이 있다면, 나머지 연산을 통해 3을 얻게 된다. 그다음 42를 10으로 나누면 나머지가 2이고, 몫이 4가 된다. 자연스럽게 나머지 연산을 통해 얻은 숫자를 결과 앞에 덧붙이려고 할 것이다. 하지만 문자열의 앞에 숫자를 덧붙이려면 남아 있는 숫자를 한 칸씩 뒤로 움직여야 하므로 비효율적이다. 더 효율적인 방법은 차례대로 문자열 뒤에 덧붙인 다음, 마지막에 역순으로 배열된 문자열을 한 번 뒤집어 주면 된다.

x가 음수라면 x를 양수로 바꾼 뒤, 마지막에 '-'를 붙여 주기만 하면 된다. x가 0일 때는 결과가 공백이므로 명시적으로 0을 적어 줘야 한다.

문자열을 정수로 바꿀 때는 자릿수 시스템을 그대로 이용하면 된다. 10진수 숫자 d2d1d0는 10^2*d2 + 10^1*d1 + d0로 표현된다. 무식한 방법으로 생각해 보면 가장 오른쪽에 있는 숫자부터 시작해서 10^i*di를 곱해 주면 된다.

이보다 더 근사한 해법이 있다. 오른쪽이 아니라 가장 왼쪽의 숫자부터 계산을 시작하는 것이다. 즉, 중간 결괏값에 10을 곱한 뒤 각 자릿수를 더해 나간다. 예를 들어 "314"를 정수로 바꾼다고 가정하자. 중간 결괏값 r은 0으로 초기화한다. 첫 번째 반복에서 r=3이 된다. 두 번째 반복에서 r=3*10+1=31이 되고, 세 번째 반복에서 r=31*10+4=314가 된다.

음수의 경우에는, 부호를 기억한 뒤 마지막 결과를 음수로 바꿔 주면 된다.

```java
public static String intToString(int x) {
    boolean isNegative = false;
    if (x < 0) {
        isNegative = true;
    }

    StringBuilder s = new StringBuilder();
    do {
        s.append((char)('0' + Math.abs(x % 10)));
        x /= 10;
    } while (x != 0);

    if (isNegative) {
        s.append('-');
    }
    s.reverse();
    return s.toString();
}

public static int stringToInt(String s) {
    int result = 0;
    for (int i = s.charAt(0) == '-' ? 1 : 0; i < s.length(); ++i) {
        final int digit = s.charAt(i) - '0';
        result = result * 10 + digit;
    }
    return s.charAt(0) == '-' ? -result : result;
}
```

## 6.2 밑수 바꾸기
10진수 시스템의 자릿수는 10의 승수를 결정하는 데 사용된다. 예를 들어 "314"는 3 * 100 + 1 * 10 + 4 * 1을 의미한다. 10진수 시스템을 밑수가 b인 숫자 시스템으로 일반화할 수 있다. 0 <= ai < b일 때 문자열 "ak-1ak-2...a1a0"은 b진수 시스템에서는 a0 * b^0 + a1 * b^2 + ... + ak-1 * b^(k-1)을 의미한다.

문자열 하나와 두 개의 정수 b1, b2가 주어졌을 때, 정수의 밑수를 바꾸는 프로그램을 작성하라. 밑수가 b1인 입력 문자열을 밑수가 b2인 문자열로 바꾸면 된다. 2 <= b1, b2 <= 16이고, "A"는 10, "B"는 11, ..., "F"는 15를 나타낸다(예를 들어 문자열이 "615"이고, b1은 7, b2는 13일 때 결과는 "1A7"이 된다. 왜냐하면 6 * 7^2 + 1 * 7 + 5 = 1 * 13^2 + 10 * 13 + 7이기 때문이다).

> 힌트: 우리가 주로 사용하는 밑수는 무엇인가.

우선 무식하게 접근해보자. 입력 숫자를 1진수로 바꾼 뒤 1을 b2, b2^2, b2^3 등의 배수로 그룹을 지으면 된다. 예를 들어 (102)_3 = (11111111111)_1이 된다. 이를 밑이 4인 숫자로 바꾸면, 1의 개수가 4개인 그룹 2개가 생기고, 나머지 1이 3개 남는다. 따라서 그 결과는 (23)_4가 된다. 이 방법은 구현하기 힘들고 시간 밑 공간 복잡도도 굉장히 크다.

모든 언어에는 정수형 변수가 존재한다. 즉, 모든 언어는 곱셈, 덧셈, 나눗셈, 나머지 등과 같은 산순 연산을 제공한다. 이 사실을 통해 더 쉽게 밑수를 바꾸는 알고리즘을 개발할 것이다. 즉, 곱셈과 덧셈을 통해 밑수가 b1인 문자열을 정수로 바꾸고, 나머지 연산과 나눗셈 연산을 통해 해당 정수를 밑수가 b2인 문자열로 바꿀 것이다. 예를 들어 문자열이 "615"이고 b1 = 6, b2 = 13이라고 가정하자. 이를 10진수로 표현하면 306이 된다. 306을 13진수로 표현했을 때의 최하위 숫자는 306 mod 13 = 7이고, 나머지 몫은 306/13 = 23이 된다. 그 다음에 등장할 숫자는 23 mod 13 = 10, 즉 'A'가 된다. 23/13 = 1이고 1 mod 13 = 1이므로 마지막 숫자는 1이 된다. 따라서 최종 결과는 "1A7"이 된다. 밑수를 바꾸는 알고리즘은 더 작은 부분 문제로 간단하게 표현되므로 자연스럽게 재귀를 사용하면 좋다.

```java
public static String convertBase(String numAsString, int b1, int b2) {
    boolean isNegative = numAsString.startsWith("-");
    int numAsInt = 0;
    for (int i = (isNegative ? 1 : 0); i < numAsString.length(); i++) {
        numAsInt *= b1;
        numAsInt += Character.isDigit(numAsString.charAt(i))
            ? numAsString.charAt(i) - '0'
            : numAsString.charAt(i) - 'A' + 10
    }
    return (isNegative ? "-" : "") + (numAsInt == 0 ? "0" : constructFromBase(numAsInt, b2))
}

public static String constructFromBase(int numAsInt, int base) {
    return numAsInt == 0
        ? ""
        : constructFromBase(numAsInt / base, base) + (char)(numAsInt % base >= 10 ? 'A' + numAsInt % base - 10 : '0' + numAsInt % base);
}
```

s의 길이를 n이라고 했을 때 시간 복잡도는 O(n(1 + log_b2(b1))), 즉 O(nlog_b2(b1))이 된다. 그 이유는 다음과 같다. 먼저 s에서 x를 얻기 위해서 b개의 곱셈과 덧셈을 수행한다. 그리고 최종 결과를 얻기 위해서 log_b2^x만큼의 곱셈과 덧셈을 수행한다. x의 상한은 b1^n이고 log_b2(b1^n) = n log_b2(b1)가 된다.