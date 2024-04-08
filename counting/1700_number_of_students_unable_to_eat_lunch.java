class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int circles = 0, squares = 0;

        for (int student : students) {
            if (student == 0) {
                circles++;
            } else {
                squares++;
            }
        }

        for (int sandwich : sandwiches) {
            if (sandwich == 0 && circles == 0) return squares;
            if (sandwich == 1 && squares == 0) return circles;

            if (sandwich == 0) {
                circles--;
            } else {
                squares--;
            }
        }
        return 0;
    }
}