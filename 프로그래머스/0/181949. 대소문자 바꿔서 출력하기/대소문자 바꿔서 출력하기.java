import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        for(int i=0; i<a.length(); i++){
            if( (int)a.charAt(i) >= 97){
                System.out.print((char)((int)a.charAt(i) - 32));
            }else{
                System.out.print((char)((int)a.charAt(i) +32));
            }
        }
    }
}