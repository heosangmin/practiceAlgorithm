package java_epi.ch04;

public class Divide {
    
    /*
        무식한 방법으로 풀면 x가 y보다 크기가 작아질 때까지 x에서 y를 반복해서 빼면 된다.
        하지만 x가 크고 y가 작을수록 비효율적이다.

        이 방식을 개선하면 더 효율적인 알고리즘을 찾을 수 있다. 예를 들어 (2^k)y <= x를 만족하는 가장 큰 k를 찾을 뒤 x에서 (2^k)y를 빼고, 2^k를 몫에 더한다. 즉, x = (1011)2, y = (10)2이라고 할때 k는 2가 된다(왜냐하면 2*(2^2) <= 11이고, 2*(2^3) > 11이므로). 그리고 (11)2을 이용해서 이 과정을 반복한다.

        이 방식은 반복할 때마다 x의 크기가 최소 절반씩 줄어들기 때문에 굉장히 효율적이며 빠르다. n을 x/y 결괏값의 길이라고 했을 때, 총 O(n)만큼의 반복이 필요하고, 각 반복마다 (2^k)y <= x를 만족하는 가장 큰 k를 찾는 데 O(n)만큼의 시간이 소요되므로 총 시간 복잡도는 O(n^2)이 된다.

        x보다 작거나 같은 k를 찾을 때 (2^0)y, (2^1)y, (2^2)y, ...와 같이 증가하는 순서대로 찾기보다는, 초반에 (2^k)y <= x를 만족하는 가장 큰 k를 찾은 뒤 그 다음부터는 (2^(k-1))y, (2^(k-2))y, ...의 순서대로 k를 감소시켜 가면서 k를 찾으면 더 효율적이다.
    */

    public static long divide(long x, long y) {
        long result = 0;
        int power = 32;
        long yPower = y << power;
        while ( x >= y ) {
            while (yPower > x) {
                yPower >>>= 1;
                --power;
            }

            result += 1 << power;
            x -= yPower;
        }
        return result;
    }

    public static void main(String[] args) {
        
    }
}
