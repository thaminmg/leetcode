class MyStack {

    private Queue<Integer> queue1, queue2;
    private int top;
    
    public MyStack() {
        queue1 = new LinkedList<Integer>();
        queue2 = new LinkedList<Integer>();
    }
    
    public void push(int x) {
        queue1.offer(x);
        top = x;
    }
    
    public int pop() {
        while (queue1.size() > 1) {
            queue2.offer(queue1.poll());
        }
        int res = queue1.poll();
        while (!queue2.isEmpty()) {
            if (queue2.size() == 1) {
                top = queue2.peek();
            }
            queue1.offer(queue2.poll());
        }

        return res;
    }
    
    public int top() {
        return top;
    }
    
    public boolean empty() {
        return queue1.isEmpty();   
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */