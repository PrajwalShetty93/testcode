import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        Map<String, Integer> alphaCountMap= new HashMap<>();
        for(int i=0;i<s.length();i++)
        {   
            String chr  = Character.toString(s.charAt(i));
            if(alphaCountMap.containsKey(chr))
            {
                alphaCountMap.put(chr, alphaCountMap.get(chr)+1);
            }
            else
            {
                alphaCountMap.put(chr,1);
            }
        }

        for(int i=0;i<t.length();i++)
        {
            String chr  = Character.toString(t.charAt(i));
            if(alphaCountMap.containsKey(chr))
            {
                alphaCountMap.put(chr, alphaCountMap.get(chr)-1);
            }
            else
            {
                return false;
            }
        }

        for (String key : alphaCountMap.keySet())
        {
            if(alphaCountMap.get(key)>0)
            {
                return false;
            }
        }

        
        return true;
    }



    public static void main(String[] args)
    {
    String s="racecar";
    String t="carrace";
    Solution sol = new Solution();
    Boolean result = sol.isAnagram(s, t);
    System.out.println(result);
    }

}
