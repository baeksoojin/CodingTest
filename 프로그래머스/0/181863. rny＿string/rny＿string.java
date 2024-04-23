class Solution {
    public String solution(String rny_string) {
        String result = "";
        // 탐색하면서 m일때는 answer에 rn을 넣어주면 됨. 완전탐색
        
        for(char data: rny_string.toCharArray()){
            if(data == 'm'){
                result += "rn";
            }else{
                result += data;
            }
            
        }
        
        return result;
    }
}