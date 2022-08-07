import java.util.*;
public class A_Is_your_horseshoe_on_the_other_hoof {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=sc.nextInt();
        int d=sc.nextInt();
        Set<Integer> st=new HashSet<Integer>();
        st.add(a);
        st.add(b);
        st.add(c);
        st.add(d);
        System.out.println(4-st.size());
    }
    
}