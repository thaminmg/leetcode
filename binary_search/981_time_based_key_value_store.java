class TimeMap {

    private HashMap<String, ArrayList<Pair<Integer, String>>> mappings;

    public TimeMap() {
        mappings = new HashMap<String, ArrayList<Pair<Integer, String>>>();
    }
    
    public void set(String key, String value, int timestamp) {
      
        if (!mappings.containsKey(key)) {
            mappings.put(key, new ArrayList());
        } 
        mappings.get(key).add(new Pair(timestamp, value));        
    }
    
    public String get(String key, int timestamp) {
        if (!mappings.containsKey(key)) return "";
        if (timestamp < mappings.get(key).get(0).getKey()) return "";

        int n = mappings.get(key).size();
        int left = 0, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;

            if (mappings.get(key).get(mid).getKey() <= timestamp) {
                left = mid + 1;
            } else{
                right = mid;
            }
        }
        if (right == 0) return "";
        return mappings.get(key).get(right - 1).getValue();
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */