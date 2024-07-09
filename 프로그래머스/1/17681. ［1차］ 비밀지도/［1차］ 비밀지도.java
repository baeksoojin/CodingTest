import java.util.*;

class Solution {
    
    public String[] numToBinary(int[] arr){
        
        String[] binarys = new String[arr.length];
        for(int i=0; i<arr.length; i++){
            int num = arr[i];
            String binary = "";
            while((int)(num/2) !=0){
                
                binary += String.valueOf((int)(num%2));
                num = (int)(num/2);
            }
            binary += num;
            
            StringBuffer result = new StringBuffer(binary);
            String reversedStr = result.reverse().toString();
            binary = String.format("%" + arr.length + "s", reversedStr.replace(' ', '0'));
            binarys[i] = binary;
        }
        
        return binarys;
        
        
    }
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        
        // 1. 각 숫자를 2진수로 변경
        String[] binary1 = numToBinary(arr1);
        String[] binary2 = numToBinary(arr2);
        
        System.out.println(Arrays.toString(binary1));
        
        // 2. 빈 2차원 배열에 이진수 비트 or 연산을 진행
        
        
        for(int i=0; i<n; i++){
            String map = "";
            for(int j=0; j<n; j++){
                
                if(binary1[i].charAt(j)=='1' || binary2[i].charAt(j) == '1'){ // or 연산 -> 1
                    map+="#";
                }else{
                    map+=" ";
                }
            }
            answer[i] = map;
        }
        
        
        return answer;
    }
}