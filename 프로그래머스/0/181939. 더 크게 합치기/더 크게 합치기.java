import java.util.*;

class Solution {
    
    
    public int solution(int a, int b) {
    
        String[] numbersStr = {String.valueOf(a), String.valueOf(b)};

        Arrays.sort(numbersStr, (x,y) -> (y.repeat(4)).compareTo(x.repeat(4)));
        
        return Integer.valueOf(numbersStr[0] + numbersStr[1]);
    }
}