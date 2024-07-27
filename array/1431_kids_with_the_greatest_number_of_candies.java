class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int n = candies.length;
        List<Boolean> res = new ArrayList();
        int max = Integer.MIN_VALUE;
        for (int candy : candies) {
            max = Math.max(candy, max);
        }

        for (int candy : candies) {
            res.add(candy + extraCandies >= max);
        }
        return res;
    }
}