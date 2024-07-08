import java.util.*;

class Solution {
    
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        
        int left = 0, right =  distance;
        Arrays.sort(rocks);
        
        while(left<=right){
            int mid = (int)((left+right)/2);
            int before = 0, smallCount = 0;
            
            for(int rock :rocks){
                int diff = rock - before;
                if(diff < mid){
                    smallCount +=1;
                }else{
                    before = rock;
                }
            }
            
            int diff = distance - before;
            if(diff < mid){
                smallCount +=1;
            }
            
            if(smallCount > n){
                right = mid-1;
            }else{
                left=mid+1;
                answer = mid;
            } 
            
        }
        
        return answer;
    }
}