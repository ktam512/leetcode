import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, "", 0, 0, n);
        return result;
    }

    private void backtrack(List<String> result, String s, int open, int close, int n) {
        if (s.length() == 2 * n) { // Base case: when the length of the string is equal to 2*n
            result.add(s);
            return;
        }
        if (open < n) { // If the count of '(' is less than n, we can add '('
            backtrack(result, s + '(', open + 1, close, n);
        }
        if (close < open) { // If the count of ')' is less than the count of '(' already added, we can add ')'
            backtrack(result, s + ')', open, close + 1, n);
        }
    }
}
