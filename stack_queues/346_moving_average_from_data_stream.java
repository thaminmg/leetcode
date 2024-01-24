class MovingAverage {

    private Queue<Integer> q;
    private int qSize;
    public MovingAverage(int size) {
        q = new LinkedList<Integer>();
        qSize = size;
    }
    
    public double next(int val) {
        if (q.size() < qSize) {
            q.offer(val);
        } else {
            q.poll();
            q.offer(val);
        }
        int total = 0;
        for (Integer item: q) {
            total += item;
        }
    
        return (double) total / q.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */