class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int n = 0; n < nums.length; n++) {
            if (seen.contains(nums[n])) {
                return true;
            }
            seen.add(nums[n]);
        }
        return false;
    }
}