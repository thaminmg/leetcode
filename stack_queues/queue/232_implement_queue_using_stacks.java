class MyQueue {

    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    private int front; 
    
    public MyQueue() {
        stack1 = new Stack<Integer>();
        stack2 = new Stack<Integer>();
        
    }   
    
    public void push(int x) {
        if (stack1.empty()) front = x;
        
        while (!stack1.empty()) {
            stack2.push(stack1.pop());
        }
        stack2.push(x);
        while (!stack2.empty()) {
            stack1.push(stack2.pop());
        }

    }
    
    public int pop() {
        int res = stack1.pop();
        if (!stack1.empty()) {
            front = stack1.peek();    
        }
        return res;
    }
    
    public int peek() {
        return front;
    }
    
    public boolean empty() {
        return stack1.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */