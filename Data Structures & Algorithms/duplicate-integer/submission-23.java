class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            int currentElement = nums[i];
            if (seen.contains(currentElement)) {
                return true;
            }
            seen.add(currentElement);
        }

        return false;
    }
}