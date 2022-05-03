package java_epi.ch04;

public class Reverse {

    /*
        비트 연산과 관계 있는줄 알고 이건 또 뭐지 싶었는데 꾀가 필요한 정도였다.
        1. 주어진 정수를 10으로 나눈 나머지가 마지막 자리의 숫자이고
        2. 주어진 정수를 10으로 나눈 몫이(123 / 10 = 12) 다시 1의 계산 대상이 된다.

        리턴하기 전, 원래 정수가 음수였으면 결과도 음수로 리턴한다.

        이건 재미 있는 문제다.
    */

    public static long reverse(int x) {
        long result = 0;
        long xRemaining = Math.abs(x);
        while (xRemaining != 0) {
            result = result * 10 + xRemaining % 10;
            xRemaining /= 10;
        }
        return x < 0 ? -result : result;
    }

    public static long reverse_bf(int x) {
        String inp = Integer.toString(x);
        String oup = "";
        for (int i = inp.length()-1; i >= 0; i--) {
            if (inp.charAt(i) != '-') {
                oup += inp.charAt(i);
            } else {
                oup = inp.charAt(i) + oup;
            }
        }
        return Integer.parseInt(oup);
    }

    public static void main(String[] args) {
        System.out.println(reverse(1234));
        System.out.println(reverse(-1234));
    }
}