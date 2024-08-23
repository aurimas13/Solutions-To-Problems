class Solution {
    public String fractionAddition(String expression) {
        // Add '+' at the beginning if the expression doesn't start with a sign
        if (expression.charAt(0) != '+' && expression.charAt(0) != '-') {
            expression = "+" + expression;
        }
        
        // Parse fractions
        List<int[]> fractions = new ArrayList<>();
        int i = 0;
        while (i < expression.length()) {
            int sign = expression.charAt(i) == '+' ? 1 : -1;
            i++;
            int j = i;
            while (j < expression.length() && expression.charAt(j) != '+' && expression.charAt(j) != '-') {
                j++;
            }
            String[] parts = expression.substring(i, j).split("/");
            int num = Integer.parseInt(parts[0]);
            int den = Integer.parseInt(parts[1]);
            fractions.add(new int[]{sign * num, den});
            i = j;
        }
        
        // Sum all fractions
        int numerator = 0, denominator = 1;
        for (int[] fraction : fractions) {
            int num = fraction[0], den = fraction[1];
            numerator = numerator * den + num * denominator;
            denominator *= den;
            int g = gcd(Math.abs(numerator), denominator);
            numerator /= g;
            denominator /= g;
        }
        
        // Convert result to string format
        return numerator + "/" + denominator;
    }
    
    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}