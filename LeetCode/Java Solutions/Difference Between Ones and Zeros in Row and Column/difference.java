import java.util.*;

class Solution {
    private Map<String, List<Integer>> memo = new HashMap<>();
    
    public List<Integer> diffWaysToCompute(String expression) {
        return compute(expression);
    }
    
    private List<Integer> compute(String expr) {
        if (memo.containsKey(expr)) {
            return memo.get(expr);
        }
        
        List<Integer> results = new ArrayList<>();
        
        if (expr.matches("\\d+")) {
            results.add(Integer.parseInt(expr));
            return results;
        }
        
        for (int i = 0; i < expr.length(); i++) {
            char c = expr.charAt(i);
            if (c == '+' || c == '-' || c == '*') {
                List<Integer> left = compute(expr.substring(0, i));
                List<Integer> right = compute(expr.substring(i + 1));
                
                for (int l : left) {
                    for (int r : right) {
                        switch (c) {
                            case '+':
                                results.add(l + r);
                                break;
                            case '-':
                                results.add(l - r);
                                break;
                            case '*':
                                results.add(l * r);
                                break;
                        }
                    }
                }
            }
        }
        
        memo.put(expr, results);
        return results;
    }
}