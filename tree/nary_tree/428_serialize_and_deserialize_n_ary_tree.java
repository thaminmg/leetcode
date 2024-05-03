// /*
// // Definition for a Node.
// class Node {
//     public int val;
//     public List<Node> children;

//     public Node() {}

//     public Node(int _val) {
//         val = _val;
//     }

//     public Node(int _val, List<Node> _children) {
//         val = _val;
//         children = _children;
//     }
// };
// */

class Codec {
    // Encodes a tree to a single string.
    public String serialize(Node root) {
        StringBuilder sb = new StringBuilder();
        rserialize(root, sb);
        return sb.toString();       
    }

    public void rserialize(Node root, StringBuilder sb) {
        if (root == null) return;

        sb.append((char) (root.val + '0'));
        for (Node child : root.children) {
            rserialize(child, sb);
        }
        sb.append('#');
    }
	
    // Decodes your encoded data to tree.
    public Node deserialize(String data) {
        if (data.isEmpty()) return null;
        return rdeserialize(data, new int[1]);
    }

    public Node rdeserialize(String data, int[] index) {
        if (index[0] == data.length()) return null;
        Node node = new Node(data.charAt(index[0]) - '0', new ArrayList<Node>());
        index[0]++;
        while (data.charAt(index[0]) != '#') {
            node.children.add(rdeserialize(data, index));
        }
        index[0]++;
        return node;
    }
}

// // Your Codec object will be instantiated and called as such:
// // Codec codec = new Codec();
// // codec.deserialize(codec.serialize(root));
