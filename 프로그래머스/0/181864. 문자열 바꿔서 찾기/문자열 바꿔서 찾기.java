class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        
        // 변경한 문자열 만들기
        String stringTemp = "";
        
        for(char c : myString.toCharArray()){
            if(c=='B'){
                stringTemp +='A';
                continue;
            }
            if(c=='A'){
                stringTemp += 'B';
                continue;
            }
            stringTemp += c;
        }
        System.out.println(stringTemp);
        System.out.println(stringTemp.length()-pat.length());
        
        // pat이 존재하는지 찾기
        
        for(int i=0; i<stringTemp.length()-pat.length()+1; i++){
            String string1 = stringTemp.substring(i,i+pat.length());
            int flag = string1.equals(pat) ? 1 : 0;
            if(flag == 1){
                return flag;
            }
        }
        return 0;
    }
}