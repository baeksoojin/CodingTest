import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        
        Arrays.sort(num_list);
         System.out.println(num_list.length);
        
        int[] newList = new int[num_list.length-5];
        
        for(int i=0; i<num_list.length-5; i++){
            newList[i] = num_list[i+5];
        }
        

        return newList;
    }
}