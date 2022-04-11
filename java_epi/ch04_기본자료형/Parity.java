package java_epi.ch04;

public class Parity {

    public static short parity_my(long x) {
        // 주어진 숫자의 패리티를 구하기 위해 2진수 1비트의 개수를 세어야 한다.
        // 가장 효율적인 방법은 모르겠지만
        // 입력 값을 어떻게든 2진수로 바꾸고 거기서 1의 개수를 셀 수 있겠지.
        short result = 0;
        int count = 0;
        char[] bits = Long.toBinaryString(x).toCharArray();
        for(char bit : bits) {
            if (bit == '1') {
                result++;
            }
            count++;
        }
        System.out.println("count: " + count);
        return (short) (result % 2);
    }

    public static short parity_1(long x) {
        // >>>= 연산은 >>=와 뭐가 다르지? 검색해보니 >>> 연산은 부호 비트와 상관 없이(unsigned) lmb를 0으로 채운다고 한다.
        // 최하위 비트에 1이 등장할 때마다 result를 xor한다. 결국 1이 홀수 개일때 패리티 1이 반환됨.
        // 입력 크기가 n일 때, 시간은 O(n)만큼 걸린다.
        short result = 0;
        int count = 0;
        while (x != 0) {
            result ^= (x & 1);
            x >>>= 1;
            count++;
        }
        System.out.println("count: " + count);
        return result;
    }

    /*
        더 나은 방법으로,
        x & (x - 1)은 1로 세팅된 비트 중 가장 낮은 비트를 지우는 것과 같다. 예를 들어, x = 0b00101100일때, x - 1 = 0b00101011과 같다. 따라서 x & (x - 1) = 0b00101100 & 0b00101011 = 0b00101000이 된다. 이 비트 조작 트릭을 기억해 두면 시간 복잡도를 줄이는 데 사용할 수 있다. k가 1로 세팅된 비트의 개수라고 하면(예를 들어, 10001010의 경우에 k = 3이다.) 시간 복잡도는 O(k)가 된다.
    */
    public static short parity_2(long x) {
        // x &= (x - 1)로 인해 1비트의 수만큼만 반복을 한다. -> 저 연산은 x의 2진수에서 1로 세팅된 비트수를 하나 줄여주는 트릭이다.
        // 즉 반복마다 result를 반전시키는 것으로 끝.
        short result = 0;
        int count = 0;
        while (x != 0) {
            result ^= 1;
            x &= (x - 1); // x의 하위 비트를 지운다.
            count++;
        }
        System.out.println("count: " + count);
        return result;
    }

    /*
        다른 관점의 접근법을 고려해 보자. 원래 풀려던 문제는 매우 큰 수에 대한 패리티를 어떻게 구하는가였다. 여기에는 두 가지 방법이 있다. 이 방법들은 일반적으로 많은 수의 비트 연산을 효율적으로 수행하는 데도 쓸 수 있다. 하나는 다수의 비트를 한 번에 처리하는 방법이고, 다른 하나는 연산 결과를 룩업테이블(lookup table)에 캐시 형태로 저장하는 방법이다.

        먼저 캐시 형태로 저장하는 방법을 살펴보자. 물론 64비트의 패리티 값을 캐시에 모두 저장할 수는 없다. 64비트의 패리티 값을 모두 저장하려면 2^64비트의 저장 공간이 필요한데, 이 크기는 10조 엑사바이트(exabyte) 정도가 된다. 우선 패리티가 가진 하나의 성질을 생각해보자. 어떤 그룹의 패리티를 계산하고자 할 때, 그 그룹을 나누는 순서는 아무래도 상관이 없다. 즉 결합법칙( (a+b)+c = a+(b+c) )이 성립한다. 따라서 64개의 비트 숫자를 16비트 숫자 4개로 나눈 후, 각 숫자의 패리티 값을 구하고, 여기서 나온 4개의 패리티 값의 패리티를 구하면 된다. 16이라는 숫자를 선택한 이유는 2^16=65536은 상대적으로 작아서 배열에 저장할 수 있기 때문이다. 또한 64가 16으로 나누어 떨어지므로 10비트씩 나눌 때보다 코드가 더 간단하다.

        2비트 숫자의 룩업테이블을 사용해보자. (00)2, (01)2, (10)2, (11)2의 패리티는 <0,1,1,0>이므로 이 값을 캐시에 넣는다. (11001010)2의 패리티를 구하기 위해서는 (11)2, (00)2, (10)2, (10)2의 패리티를 계산하면 된다. 룩업테이블을 통해 이 값들이 각각 0,0,1,1 이라는 사실을 알 수 있으므로 최종 결과는 0,0,1,1의 패리티인 0이 된다.

        [마스크에 대한 설명은 생략]
    */
    // public static short parity_3(long x) {
    //     final int WORD_SIZE = 16;
    //     final int BIT_MASK = 0xFFFF;
    //     return (short) (
    //         precomputedParity[(int)(x >>> (3 * WORD_SIZE)) & BIT_MASK]
    //         ^ precomputedParity[(int)(x >>> (2 * WORD_SIZE)) & BIT_MASK]
    //         ^ precomputedParity[(int)(x >>> (WORD_SIZE)) & BIT_MASK]
    //         ^ precomputedParity[(int)x & BIT_MASK];
    //     );
    // }

    /*
        XOR의 속성을 이용하면 시간 복잡도를 개선할 수 있다.
        XOR는 결합법칙과 계산 순서를 바꾸어도 전체 결과가 같다는 교환법식을 만족하는데, 이 법칙을 사용하면 CPU 단계의 XOR 연산에서 여러 비트를 한 번에 수행하도록 알고리즘을 개선할 수 있다.

        아래의 경우 단어의 크기가 n일 때 시간 복잡도가 O(log n)이 된다.
        이 알고리즘을 캐시와 결합해서도 사용할 수 있다. 즉, 룩업테이블을 통해 16비트의 패리티 값을 가져올 수 있다.
    */
    public static short parity_4(long x) {
        x ^= x >>> 32;
        x ^= x >>> 16;
        x ^= x >>> 8;
        x ^= x >>> 4;
        x ^= x >>> 2;
        x ^= x >>> 1;
        return (short)(x & 0x1);
    }

    public static void main(String[] args) {
        String format = "input: %d(%s), output: %d";
        long value = 129L;
        System.out.println(String.format(format, value, Long.toBinaryString(value), Parity.parity_my(value)));
        System.out.println(String.format(format, value, Long.toBinaryString(value), Parity.parity_1(value)));
        System.out.println(String.format(format, value, Long.toBinaryString(value), Parity.parity_2(value)));
        
    }
}