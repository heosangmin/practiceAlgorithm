package java_epi.ch07;

public class practice1 {
    public static void main(String[] args) {
        
        int[] n = {1,2,3,4,5,6,7};
        ListNode<Integer> L1 = new ListNode<Integer>();
        ListNode<Integer> p = L1;
        for (int x : n) {
            p.data = x;
            p.next = new ListNode<Integer>();
            p = p.next;
        }

        p = L1;
        while (p.next != null) {
            System.out.println(p.data);
            p = p.next;
        }

        System.out.println(L1);
        System.out.println(p);
        System.out.println(L1 == p);
        p = L1;
        System.out.println(L1 == p);
    }
}
