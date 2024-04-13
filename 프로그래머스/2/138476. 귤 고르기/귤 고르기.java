/**
귤 중에서 k개를 선택할 수 있는데 k개의 종류가 최소가 되도록 하기
그리디 정렬문제.
**/

import java.util.*;


class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
      
        
        // 귤의 사이즈는 필요없고 귤의 사이즈별 count개수를 배열에 저장하고 내림차순으로 정렬한다.
    
        int[] tangerineCount = new int[10000001];
        for(int i=0; i<tangerine.length; i++){
            tangerineCount[tangerine[i]] = tangerineCount[tangerine[i]]+1;
        }
        
        List<Integer> tangerineCountList = new ArrayList<>();
        long sum = 0;
        for (int value : tangerineCount) {
            if(value!=0){
                sum+=value;
                tangerineCountList.add(value);
            }
        }
        

        // 리스트 뒤집기
        Collections.sort(tangerineCountList);
        Collections.reverse(tangerineCountList);
        int count = tangerineCountList.size();
        
        
        int start =0;
        int end= 0;
        

        sum=0;
       
        for(int i=0; i<count; i++){
            sum += tangerineCountList.get(i);
            k -= tangerineCountList.get(i);
            if (k <=0){
                return i+1;
            }
        }
        
        return answer;
        
        
    }
}