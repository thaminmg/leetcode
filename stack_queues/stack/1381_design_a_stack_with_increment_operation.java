class CustomStack {

    private int[] data;
    private int stackSize;
    private int pointer;

    public CustomStack(int maxSize) {
        data = new int[maxSize];
        stackSize = maxSize;
        pointer = -1;
    }
    
    public void push(int x) {
        if (pointer + 1 < stackSize) {
            pointer++;
            data[pointer] = x;
        }
    }
    
    public int pop() {
        if (pointer == -1) {
            return - 1;
        }
        int value = data[pointer];
        pointer--;
        return value;
    }
    
    public void increment(int k, int val) {
        int temp = pointer;

        for (int i = 0; i < k; i++) {
            if (i <= pointer) {
                data[i] += val;
            } else {
                break;
            }
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */