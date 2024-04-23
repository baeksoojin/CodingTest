class Solution {
    public int solution(int[][] sizes) {
 
        
        // 가장 큰 값을 가지는 길이를 찾고 max_value
        
        int max_value = -1;
        for(int i=0; i<sizes.length; i++){
            int max_temp = sizes[i][0] < sizes[i][1] ? sizes[i][1]:sizes[i][0];
            max_value = max_temp > max_value? max_temp: max_value;
        }
        
        //가로와 세로 중에서 작은 값 중에서 가장 큰 값이 min_value
        
        int max_value2 = -1;
        for(int[] data: sizes){
            
            int min_value = data[0] < data[1]? data[0]: data[1];
            max_value2 = max_value2 < min_value ? min_value: max_value2;
            
        }
        
        return max_value*max_value2;
    }
}