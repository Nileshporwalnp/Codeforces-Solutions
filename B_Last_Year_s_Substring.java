/**
 * B_Last_Year_s_Substring
 */
import java.util.*;
public class B_Last_Year_s_Substring {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            String s=sc.next();
            if(s.substring(s.length()-4,s.length()).equals("2020")){
                System.out.println("YES");
            }
            else if(s.substring(0,4).equals("2020")){
                System.out.println("YES");
            }
            else if (s.substring(0,1).equals("2") && s.substring(s.length()-3,s.length()).equals("020")){
                System.out.println("YES");
            }
            else if (s.substring(0,2).equals("20") && s.substring(s.length()-2,s.length()).equals("20")){
                System.out.println("YES");
            }
            else if (s.substring(0,3).equals("202") && s.substring(s.length()-1,s.length()).equals("0")){
                System.out.println("YES");
            }
            else{
                System.out.println("NO");
            }
        }
    }
}