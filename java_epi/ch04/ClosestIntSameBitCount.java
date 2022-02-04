package java_epi.ch04;

public class ClosestIntSameBitCount {
    /*
        k1에 위치한 비트와 k2에 위치한 비트를 맞바꾼다고 생각해보자.(단, k1 > k2)
        이 경우에 기존 값과 새로운 값의 차이는 2^k1 - 2^k2가 된다.
        2^k1 - 2^k2를 최소화하기 위해서는 가능하면 k1을 최소한으로 해야하고 k2를 k1과 가깝게 놓아야 한다.

        무게를 같게 유지해야 하므로 k1의 비트는 k2의 비트와 달라야 한다.
        그렇지 않으면 이 둘을 뒤집었을 때 무게가 달라진다.
        즉, k1은 최하위 비트와 다르면서 가장 오른쪽에 위치한 비트여야 하고, k2는 바로 그 다음 비트여야 한다.
        정리해 보면, 서로 다른 연속한 두 비트 중에 가장 오른쪽에 있는 두 비트를 스왑하면 된다.
    */
    public static long closestIntSameBitCount(long x) {
        final int NUM_UNSIGNED_BITS = 63;
        // x를 음이 아닌 정수라고 가정했으므로 맨 앞 비트는 0이라는 사실을 알 수 있다.
        // 그러니 63의 최하위 비트에만 집중하도록 하자.
        for (int i = 0; i < NUM_UNSIGNED_BITS - 1; ++i) {
            if ( ((x >>> i) & 1) != ((x >>> i + 1) & 1) ) {
                x ^= (1L << i) | (1L << (i + 1)); // i번째 비트와 (i + 1)번째 비트를 스왑한다.
                return x;
            }
        }

        // x의 모든 비트가 0이거나 1이면 오류를 반환한다.
        throw new IllegalArgumentException("All bits are 0 or 1");
    }

    public static void main(String[] args) {
        long x = 6;
        System.out.println(Long.toBinaryString(x) + " -> " + Long.toBinaryString(closestIntSameBitCount(x)));
    }
}
