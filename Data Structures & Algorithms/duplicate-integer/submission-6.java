class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean isDuplicate = false;
        for (int i = 0; i < nums.length; i++) {
            int currentElement = nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                if (currentElement == nums[j]) {
                    isDuplicate = true;
                }
            }
        }

        return isDuplicate;
    }
}