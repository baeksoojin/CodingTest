import java.util.*;

class Solution {
    public int solution(String s) {
        String answer = "";
        
        List<String> numbers = Arrays.asList("0","1","2","3","4","5","6","7","8","9");
        List<String> words = Arrays.asList("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine");
        
        
        String currentString = "";
        for(int i=0; i<s.length(); i++){
            currentString = currentString + s.charAt(i);
            if(words.contains(currentString)){
                int index = words.indexOf(currentString);
                answer += numbers.get(index);
                currentString = "";
            }
            else if ( numbers.contains(currentString)){
                answer += currentString;
                currentString = "";
            }

        }
        
        
        return Integer.valueOf(answer);
    }
}