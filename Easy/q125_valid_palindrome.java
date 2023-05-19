class Solution {
    public boolean isPalindrome(String s) {
        String lowerS = s.toLowerCase();
        String cleanS = lowerS.replaceAll("[^a-zA-Z0-9]", "");

        StringBuilder sb = new StringBuilder(cleanS);
        String reversedS = sb.reverse().toString();

        // return cleanS.equals(sb.reverse().toString());
        // this will return true, weird
        return cleanS.equals(reversedS);
    }

    public static void main(String[] args) {
        System.out.println(new Solution().isPalindrome("race a car"));
    }
}