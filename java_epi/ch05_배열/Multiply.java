package java_epi.ch05;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Multiply {
    
    public static List<Integer> multiply(List<Integer> num1, List<Integer> num2) {
        final int sign = num1.get(0) < 0 ^ num2.get(0) < 0 ? -1 : 1; // 한쪽만 음수면 sign을 -1로 한다.
        // sign을 따로 저장해놓고 각 리스트의 첫 수를 모두 양수로 만든다.
        num1.set(0, Math.abs(num1.get(0)));
        num2.set(0, Math.abs(num2.get(0)));

        List<Integer> result = new ArrayList<>(Collections.nCopies(num1.size() + num2.size(), 0));

        for (int i = num1.size() - 1; i >=0; --i) {
            for (int j = num2.size() - 1; j >=0; --j) {
                result.set(i + j + 1, result.get(i + j + 1) + num1.get(i) * num2.get(j));
                result.set(i + j, result.get(i + j) + result.get(i + j + 1) / 10);
                result.set(i + j + 1, result.get(i + j + 1) % 10);
            }
        }

        // 0으로 시작하는 부분을 제거한다.
        int first_not_zero = 0;
        while (first_not_zero < result.size() && result.get(first_not_zero) == 0) {
            ++first_not_zero;
        }
        result = result.subList(first_not_zero, result.size());
        if (result.isEmpty()) {
            return Arrays.asList(0);
        }
        result.set(0, result.get(0) * sign);
        return result;
    }

    public static void main(String[] args) {
        List<Integer> num1 = new ArrayList<Integer>();
        List<Integer> num2 = new ArrayList<Integer>();
        num1.add(9);
        num1.add(0);
        num1.add(0);
        num2.add(-9);
        num2.add(9);
        num2.add(9);
        List<Integer> result = multiply(num1, num2);
        result.stream().forEach(System.out::print);
    }
}
