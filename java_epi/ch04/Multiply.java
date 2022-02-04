package java_epi.ch04;

public class Multiply {

    /*
        비트 연산을 이용해서 곱셈

        결괏값을 0으로 초기화한 다음에 x의 비트를 순회하면서 x의 k번째 비트가 1로 세팅되어 있다면 (2^k)y를 더한다.
        (2^k)y는 y를 k번 시프트한 것이다.
    */
    
    public static long multiply(long x, long y) {
        long sum = 0;
        while(x != 0) {
            // x의 각 비트를 확인해 본다.
            if ((x & 1) != 0) {
                sum = add(sum, y);
            }
            x >>>= 1;
            y <<= 1;
        }
        return sum;
    }

    private static long add(long a, long b) {
        long sum = 0, carryin = 0, k = 1, tempA = a, tempB = b;
        while ( tempA != 0 || tempB != 0 ) {
            long ak = a & k, bk = b & k;
            long carryout = (ak & bk) | (ak & carryin) | (bk & carryin);
            sum |= (ak ^ bk ^ carryin);
            carryin = carryout << 1;
            k <<= 1;
            tempA >>>= 1;
            tempB >>>= 1;
        }
        return sum | carryin;
    }
    public static void main(String[] args) {
        long x = 13, y = 9;
        System.out.println("x = " + x + " * y = " + y + " = " + multiply(x, y));
    }
}
