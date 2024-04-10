import java.util.Deque;
import java.util.LinkedList;
import java.util.Arrays;

class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        Deque<Integer> revealOrder = new LinkedList<>();
        
        for (int i = deck.length - 1; i >= 0; i--) {
            if (!revealOrder.isEmpty()) {
                revealOrder.addFirst(revealOrder.removeLast());
            }
            revealOrder.addFirst(deck[i]);
        }
        
        int[] result = new int[deck.length];
        int idx = 0;
        for (int card : revealOrder) {
            result[idx++] = card;
        }
        return result;
    }
}
