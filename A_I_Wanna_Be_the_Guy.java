import javafx.scene.transform.Scale;

import java.lang.reflect.Array;
/**
 * A_I_Wanna_Be_the_Guy
 */
import java.util.*;
public class A_I_Wanna_Be_the_Guy {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        Set<Integer> st=new HashSet<>();
        int n=sc.nextInt();
        int temp=0;
        for(int i=0;i<n;++i){
            temp+=(i+1);
        }
        int s1=sc.nextInt();
        for(int i=0;i<s1;i++){
        st.add(sc.nextInt());
        }
        int s2=sc.nextInt();
        for(int i=0;i<s2;i++){
            st.add(sc.nextInt());
        }
        for (Integer k : st) {
            temp-=k;
        }
        if(temp==0){
            System.out.println("I become the guy.");
        }
        else{
            System.out.println("Oh, my keyboard!");
        }

    }
}