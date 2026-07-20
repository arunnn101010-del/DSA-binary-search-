# Promblem - find peak element 
# Approach - binary search 
# Time and space complexity - 0(log n) & 0(1) 
# Leetcode and diffculty level - 162 & medium 
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l=0, r=nums.size()-1;

        while(l < r) {
            int mid = l + (r - l) / 2;

            if(nums[mid] < nums[mid+1]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }
};
