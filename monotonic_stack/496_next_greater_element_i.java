class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] res = new int[nums1.length];
        Stack<Integer> stack = new Stack<>();
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums2.length; i++) {
            while (!stack.empty() && nums2[stack.peek()] < nums2[i]) {
                int topIndex = stack.pop();
                map.put(nums2[topIndex] , nums2[i]);
            }
            stack.push(i);
        }

        while (!stack.empty()) {
            map.put(nums2[stack.pop()], -1);
        }
       
        for (int i = 0; i < nums1.length; i++) {
            res[i] = map.get(nums1[i]);
        }
        return res;
    }
}