package java_epi.ch04;

public class ReverseBits {
    
    public static long reverseBits_0(long x) {
        // 앞선 4.2의 방법을 이용해서 상위 32비트와 하위 32비트를 스왑하기.
        int length = 64;
        for (int i = 0; i < length/2; i++) {
            int b = i;
            int a = length - i - 1;

            if ( ((x >>> a) & 1) != ((x >>> b) & 1)) {
                long bitMask = (1L << a) | (1L << b);
                x ^= bitMask;
            }
        }
        return x;
    }

    /*
        이 연산을 반복적으로 한다면, 입력의 구조에 대해 좀 더 주의 깊게 생각해 보고 캐시를 염두에 둘 필요가 있다.
        입력이 네 개의 16비트 숫자 y3, y2, y1, y0으로 구성되어 있고 y3을 최상위 비트라고 해 보자.
        이를 역순으로 표기한다면 y3은 최하위 16비트, 더 정확히 말하면 y3의 역순이 최하위 16비트가 된다.
        
        패리티를 구하는 문제 4.1과 비슷한 방법으로, 많은 역순 연산을 필요로 하는 경우에 가장 효율적인 방법은
        미리 16비트 숫자에 대한 룩업 테이블 A를 만들어 놓는 것이다. A[y]는 y를 역순으로 배열한 값이 저장되어 있다.
        이제 x의 역순은 자연스럽게 y0의 역순, y1의 역순, y2의 역순, y3의 역순이 순서대로 등장하면 된다.

        -> 16비트 정수라면 2 ** 16이므로 65536개의 값을 미리 테이블에 저장해 놓고 참조하면 된다는 뜻.

        이 알고리즘의 시간 복잡도는 문제 4.1의 해법과 동일하게 O(n/L)이다. 여기서 n은 정수의 길이, L은 캐시의 크기를 나타낸다.
    */

    private static int[] precomputeReverse;

    public static long reverseBits_1(long x) {
        final int WORD_SIZE = 16;
        final int BIT_MASK = 0xFFFF;
        return precomputeReverse[(int)(x & BIT_MASK)] << (3 * WORD_SIZE) |
               precomputeReverse[(int)((x >>> WORD_SIZE) & BIT_MASK)] << (2 * WORD_SIZE) |
               precomputeReverse[(int)((x >>> 2 * WORD_SIZE) & BIT_MASK)] << WORD_SIZE |
               precomputeReverse[(int)((x >>> 3 * WORD_SIZE) & BIT_MASK)];
    }

    public static void main(String[] args) {
        long x = -1234567890;
        System.out.println(Long.toBinaryString(x) + ", " + Long.toBinaryString(reverseBits_0(x)));
    }
}
