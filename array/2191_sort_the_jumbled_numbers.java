class Solution {
    public int[] sortJumbled(int[] mapping, int[] nums) {
        ArrayList<Integer[]> pairs = new ArrayList();

        for (int i = 0; i < nums.length; i++) {
            String number = Integer.toString(nums[i]);
            String str = "";

            for (int j = 0; j < number.length(); j++) {
                str = str + Integer.toString(mapping[number.charAt(j) - '0']);
            }
            int value = Integer.parseInt(str);
            pairs.add(new Integer[] {value, i});
        }

        Collections.sort(pairs, 
            new Comparator<Integer[]>() {
                @Override
                public int compare(Integer[] o1, Integer[] o2) {
                    return o1[0].compareTo(o2[0]);
                }
            }
        );

        int[] res = new int[nums.length];
        for (int i = 0; i < pairs.size(); i++) {
            res[i] = nums[pairs.get(i)[1]];
        }

        return res;
    }
}