# Promblem - find minimum in roated sorted array 
# Approach - binary search 
# Time and space complexity - 0(log n) & 0(1)
# Leetcode and diffculty level - 153 & medium 
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while(left < right) {
            int mid = left + (right - left) / 2;

            if(nums[mid] > nums[right]) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }
        return nums[left];
    }
};
