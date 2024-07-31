class RecentCounter {
    LinkedList<Integer> res;

    public RecentCounter() {
        this.res = new LinkedList<Integer>();    
    }
    
    public int ping(int t) {
        this.res.addLast(t);

        while (this.res.getFirst() < t - 3000) {
            this.res.removeFirst();
        }
        return this.res.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */