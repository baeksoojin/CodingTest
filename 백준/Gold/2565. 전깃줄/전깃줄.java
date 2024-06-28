import java.util.*;

public class Main {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[][] pairNumbers = new int[n+1][2];
        pairNumbers[0] = new int[]{0,-1};

        for(int i=1; i<n+1; i++){
            for(int j=0; j<2; j++){
                pairNumbers[i][j] = sc.nextInt();
            }
        }

        // 1. a를 기준으로 정렬
        Arrays.sort(pairNumbers, (a, b) -> Integer.compare(a[0], b[0]));
//        for(int i=0; i<n+1; i++){
//            System.out.println(Arrays.toString(pairNumbers[i]));
//        }

        // 2. b가 가장 긴 증가하는 수열이여야함.
        int[] dp = new int[n+1];
        dp[0] = 0;
        for(int i=1; i<n+1; i++){
            for(int j=0; j<i; j++){

                if(pairNumbers[j][1] < pairNumbers[i][1] && dp[j] >= dp[i]){
                    dp[i] = dp[j]+1;
                }
            }
        }

        // 3. print
        int result = 0;
        for(int i=1; i<n+1; i++){
            if(dp[i] > result){
                result = dp[i];
            }
        }
        System.out.println(n - result);
        sc.close();

    }
}
