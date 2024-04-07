import java.util.*;

class Solution {
    
    
    public String solution(int[] numbers) {
        
        String[] numbersStr = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            numbersStr[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(numbersStr, (a,b) -> (b+b+b).compareTo(a+a+a));
        
        if(numbersStr[0].equals("0")){
            return "0";
        }

        StringBuilder result = new StringBuilder();
        for(int i=0; i<numbersStr.length; i++){
            result.append(numbersStr[i]);
        }

        return result.toString();
    }
}