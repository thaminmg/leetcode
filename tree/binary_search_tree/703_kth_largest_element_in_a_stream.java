class Node {
    Node left, right;
    int val, cnt;
    
    Node(int val, int cnt) {
        this.val = val;
        this.cnt = cnt;
        left = null;
        right = null;
    }
}

class KthLargest {
    Node root;
    int kth;
    
    public Node insertNode(Node root, int num) {
        if (root == null) return new Node(num, 1);
        
        if (root.val < num) {
            root.right = insertNode(root.right, num); 
        } else {
            root.left = insertNode(root.left, num);
        }
        root.cnt++;
        return root;
    }
    
    public int searchKth(Node root, int k) {
        int m = root.right != null ? root.right.cnt : 0;
        
        if (k == m + 1) return root.val;
        if (k <= m) {
            return searchKth(root.right, k);
        } else {
            return searchKth(root.left, k - m - 1);
        }
    }
    
    public KthLargest(int k, int[] nums) {
        root = null;
        for (int i = 0; i < nums.length; i++) {
            root = insertNode(root, nums[i]);   
        }   
        kth = k;
    }
    
    public int add(int val) {
        root = insertNode(root, val);
        return searchKth(root, kth);
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */