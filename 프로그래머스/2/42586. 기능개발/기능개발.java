import java.util.*;

class Solution {
    
    public static int getCompleteTime(int progress, int speed){
        
        int q = (int)((100 - progress)/ speed);
        
        if ((100 - progress)% speed != 0 ){
            q +=1;}
        
        return q;
        
        
    }
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        
        ArrayList<Integer> result = new ArrayList<>();
        // 1. 최대 걸리는 시간을 저장 
        /**
        최대 걸리는 시간 -> (int)((100 - progresses ) / speeds) / 나머지가 있다면 +1
        */
    
        int n = progresses.length;
        
        int[] completeTimes = new int[n];
        
        for(int i=0; i<n; i++){ // 100시간이 최대
            completeTimes[i] = getCompleteTime(progresses[i], speeds[i]);
        }
        
        //System.out.println(Arrays.toString(completeTimes));
        
        // 2. while문을 돌면서 pop
        int idx = 0;
        int popCount = 1;
        while(true){
            if(idx > n-1){
                break;
            }
            popCount = 1;
            int idx2 = 1;
            while(idx+idx2<= n-1 && completeTimes[idx] >= completeTimes[idx+idx2]){
                popCount +=1;
                idx2+=1;
            }
            result.add(popCount);
            idx = idx + popCount;
        }
        
        return result;
    }
}