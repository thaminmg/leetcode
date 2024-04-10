class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        int n = deck.length;
        int[] res = new int[n];
        boolean skip = false;
        int deckIndex = 0, resIndex = 0;

        Arrays.sort(deck);
        
        while (deckIndex < n) {
            if (res[resIndex] == 0) {
                if (!skip) {
                    res[resIndex] = deck[deckIndex];
                    deckIndex++;
                }
                skip = !skip;
            }
            resIndex = (resIndex + 1) % n;
        }
        return res;
    }
}