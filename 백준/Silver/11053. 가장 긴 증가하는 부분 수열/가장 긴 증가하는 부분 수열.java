
import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt( sc.next());
        int[] numbers = new int[n+1];
        numbers[0] = -1;
        for(int i=1; i<n+1; i++){
            numbers[i] = sc.nextInt();
        }

        // 가장 긴 증가하는 부분 수열 dp로 체크

        int[] count = new int[n+1];
        count[0] = 0;

        for(int i=1; i<n+1; i++){
            for(int j=0; j<i; j++){
                if(numbers[i] > numbers[j] && count[i] <= count[j]) {
                    count[i] = count[j] + 1;
                }
            }
        }

        int maxValue = 0;
        for(int i=1; i<n+1; i++){
            if( maxValue < count[i]){
                maxValue = count[i];
            }
        }

        System.out.println(maxValue);

    }
}
