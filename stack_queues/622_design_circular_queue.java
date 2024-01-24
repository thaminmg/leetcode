class MyCircularQueue {
    
    private int head;
    private int tail;
    private int size;
    private Integer[] data;

    public MyCircularQueue(int k) {
        data = new Integer[k];
        head = -1;
        tail = -1;
        size = k;
    }
    
    public boolean enQueue(int value) {        
        if (this.isFull()) return false;
        if (this.isEmpty()) {
            head = 0;
        }
        
        tail++;
        if (tail == size) tail = 0;
        data[tail] = value;

        return true;
    }
    
    public boolean deQueue() {
        if (this.isEmpty()) return false;
    
        if (tail > head) {
            head ++;
        } else if (head == tail) {
            head = -1;
            tail = -1;
        } else {
             head++;
            if (head == size) head = 0;
        }
        
        return true;
    }
    
    public int Front() {
        if (this.isEmpty()) {
            return -1;
        }
        return data[head];
    }
    
    public int Rear() {
        if (this.isEmpty()) {
            return -1;
        }
        return data[tail];
    }
    
    public boolean isEmpty() {
        if (head == -1 && tail == -1) {
            return true;
        }
        return false;
    }
    
    public boolean isFull() {        
        if ((head == 0 && tail == size - 1) || (tail < head && head - tail == 1)) {
            return true;
        }
        return false;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */