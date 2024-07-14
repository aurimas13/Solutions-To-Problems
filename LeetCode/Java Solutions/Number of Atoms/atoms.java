import java.util.*;

class Solution {
    public String countOfAtoms(String formula) {
        Deque<Map<String, Integer>> stack = new LinkedList<>();
        stack.push(new HashMap<>());
        int n = formula.length();
        int i = 0;
        
        while (i < n) {
            if (formula.charAt(i) == '(') {
                stack.push(new HashMap<>());
                i++;
            } else if (formula.charAt(i) == ')') {
                Map<String, Integer> top = stack.pop();
                int j = i + 1;
                while (j < n && Character.isDigit(formula.charAt(j))) j++;
                int multiplicity = j > i + 1 ? Integer.parseInt(formula.substring(i + 1, j)) : 1;
                i = j;
                
                for (String name : top.keySet()) {
                    int v = top.get(name);
                    stack.peek().put(name, stack.peek().getOrDefault(name, 0) + v * multiplicity);
                }
            } else {
                int j = i + 1;
                while (j < n && Character.isLowerCase(formula.charAt(j))) j++;
                String name = formula.substring(i, j);
                i = j;
                while (j < n && Character.isDigit(formula.charAt(j))) j++;
                int multiplicity = j > i ? Integer.parseInt(formula.substring(i, j)) : 1;
                i = j;
                stack.peek().put(name, stack.peek().getOrDefault(name, 0) + multiplicity);
            }
        }
        
        Map<String, Integer> map = stack.pop();
        StringBuilder sb = new StringBuilder();
        for (String name : map.keySet().stream().sorted().toArray(String[]::new)) {
            sb.append(name);
            if (map.get(name) > 1) sb.append(map.get(name));
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.countOfAtoms("H2O"));           // Output: "H2O"
        System.out.println(sol.countOfAtoms("Mg(OH)2"));       // Output: "H2MgO2"
        System.out.println(sol.countOfAtoms("K4(ON(SO3)2)2")); // Output: "K4N2O14S4"
    }
}
