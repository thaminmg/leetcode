import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

class TimeMap {

    private HashMap<String, ArrayList<HashMap<Integer, String>>> mappings;

    public TimeMap() {
        mappings = new HashMap<String, ArrayList<HashMap<Integer, String>>>();
    }
    
    public void set(String key, String value, int timestamp) {
        HashMap<Integer, String> subMappings = new HashMap<Integer, String>();
        subMappings.put(timestamp, value);
        ArrayList<HashMap<Integer, String>> lst;
        if (mappings.containsKey(key)) {
            lst = mappings.get(key);
        } else {
            lst = new ArrayList<HashMap<Integer, String>>();
        }
        lst.add(subMappings);
        mappings.put(key, lst);
    }
    
    public String get(String key, int timestamp) {
        ArrayList<HashMap<Integer, String>> lst = mappings.get(key);
        int n = lst.size();

        if (n == 0) return "";

        int left = 0, right = n - 1;
        HashMap<Integer, String> curr;
        while (left < right) {
            int mid = left + (right - left) / 2;
            curr = lst.get(mid);
            
            ArrayList<Integer> keys = new ArrayList<>();
            ArrayList<String> vals = new ArrayList<>();

            for (Entry<Integer, String> entry : curr.entrySet()) {
                keys.add(entry.getKey());
                vals.add(entry.getValue());
            }

            if (keys.get(0) == timestamp) {
                return vals.get(0);
            } else if (keys.get(0) > timestamp) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        ArrayList<Integer> keys = new ArrayList<>();
        ArrayList<String> vals = new ArrayList<>();

        for (Entry<Integer, String> entry : lst.get(left).entrySet()) {
            keys.add(entry.getKey());
            vals.add(entry.getValue());
        }
        return vals.get(0);
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */