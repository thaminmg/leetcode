class MinStack {

    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    private int currMin;
    
    public MinStack() {
        stack = new Stack<Integer>();
        minStack = new Stack<Integer>();      
        currMin = Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        stack.push(val);
        if (val < currMin) {
            minStack.push(val);
            currMin = val;
        } else {
            minStack.push(currMin);
        }
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
        if (minStack.empty()) {
            currMin = Integer.MAX_VALUE;
        } else {
            currMin = minStack.peek();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek(); 
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */