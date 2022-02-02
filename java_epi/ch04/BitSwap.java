package java_epi.ch04;

public class BitSwap {
    public static long swapBits_0(long x, int i, int j) {
        // 당장 생각나는 것은 역시 x를 문자열 비트 배열로 만들고 스왑하는 거다.
        System.out.println(Long.toBinaryString(x));
        char[] bits = Long.toBinaryString(x).toCharArray();
        char temp = bits[i];
        bits[i] = bits[j];
        bits[j] = temp;
        System.out.println(String.valueOf(bits));
        return Long.parseLong(String.valueOf(bits), 2);
        // 배열을 뒤집는 것을 깜빡했다.
    }

    /*
        한 비트는 두 가지 값만 표현할 수 있으므로 단순히 맞바꾸는 것보다 더 빠르게 수행할 수 있다.
        먼저 맞바꿀 비트가 같은지 다른지부터 확인해야 한다. 만약 이 둘이 같다면 스왑할 필요가 없다.
        만약 두 비트가 다르다면, 스왑을 하는 것과 각 비트를 각자 뒤집는 것과 결과적으로 같을 것이다.
    */

    public static long swapBits_1(long x, int i, int j) {
        System.out.println(Long.toBinaryString(x));
        System.out.println(Long.toBinaryString((x >>> i) & 1));
        System.out.println(Long.toBinaryString((x >>> j) & 1));
        System.out.println(Long.toBinaryString((1L << i) | (1L << j)));
        // i번째 비트와 j번째 비트가 다른지 확인한다.
        if ( ((x >>> i) & 1) != ((x >>> j) & 1) ) {
            // 각 비트를 뒤집어서 스왑한다.
            // bitMask를 사용해서 뒤집을 비트를 선택한다.
            // x = 1일때 x^1 = 0을 만족하고,
            // x = 0일때 x^1 = 1을 만족하므로,
            // XOR을 사용해서 비트를 뒤집을 수 있다.
            long bitMask = (1L << i) | (1L << j);
            x ^= bitMask;
        }
        System.out.println(Long.toBinaryString(x));
        return x;
    }

    public static void main(String[] args) {
        int i = 1;
        int j = 6;
        long x = 73;

        String format = "i=%d, j=%d, x=%d, result=%s";
        System.out.println(String.format(format, i, j, x, Long.toBinaryString(swapBits_0(x, i, j))));
        System.out.println(String.format(format, i, j, x, Long.toBinaryString(swapBits_1(x, i, j))));
    }
}
