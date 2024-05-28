import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        // 투포인터를 사용하여 pointer1, pointer2사이의 sum을 구한다.
        // 누적값이 S보다 큰 것에 대해서 개수를 따져줘야한다. -> 개수와 포인터1, 포인터2를 변수로 생성
        // 두개가 시작지점에서 시작하고 포인터를 옮기며 오른쪽 포인터가 배열의 끝에 도달하면 끝나야한다.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] nArray = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nArray[i] = Integer.parseInt(st.nextToken());
        }

        // 부분합을 만들 수 있는 모든 경우를 투포인터를 사용해서 돌리자! -> O(n)

        int startPoint = 0, endPoint = 0;
        int sumBetweenStartAndEnd = 0;
        int min = n;
        boolean isM = false;

        while(startPoint < n){

            // next pointer 생성
            if(sumBetweenStartAndEnd >= m){ // 만약에 특정 합을 구하는거였다면 ==m으로 변경하면 됨
                min = (endPoint - startPoint) < min? (endPoint - startPoint): min ;
                isM=true;
                sumBetweenStartAndEnd -= nArray[startPoint];
                startPoint++;
            }else if(endPoint < n){// 현재 구간합이 더 작기에 오른쪽을 옮긴다.
                    sumBetweenStartAndEnd += nArray[endPoint];
                    //다음 endpoint 및 sum 계산
                    endPoint++;

            }else{
                break;
            }


        }

        if(isM==false){
            System.out.println(0);
        }else{
            System.out.println(min);
        }

    }


}