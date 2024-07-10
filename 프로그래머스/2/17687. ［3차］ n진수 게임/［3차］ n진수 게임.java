import java.util.*;

class Solution {
    
    
    public String[] convertN(int num, int n){
        
        if(num == 0){
            return new String[]{"0"};
        }
        
        StringBuilder result = new StringBuilder("");
        
        String[] alps = new String[]{"A","B","C","D","E","F"};
        
        while (num !=0){
        
            String r = (num % n <=9) ? String.valueOf(num%n) : alps[ (num%n) - 10];
            result.append(r);
            num = (int)(num / n);
        }
        
        //뒤집기
        String answer = result.reverse().toString();
        return answer.split("");
        
    }
    
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        
        
        // 현재 몇번째 값인지 체크하기 위해 m과 p를 사용. m으로 count를 나눈 나머지 -> p-1일때 t-1 -> t가 0이면 그만
        // stop 될때까지 n진수로 변환하여 for문으로 값을 answer에 더해주기
        
        
        int current10Number = 0; // 십진수
        int totalCount = 0;
        
        
        
        while(true){
            
        
            String[] nNumbers = convertN(current10Number,n);
            
            for(int i=0; i<nNumbers.length; i++){
                
                if((totalCount % m) == p-1){
                    answer += nNumbers[i];
                    t-=1;
                    if(t==0){
                        return answer;
                    }
                }
                
                totalCount+=1;
            }
            
            current10Number+=1;
            
        }
    }
}