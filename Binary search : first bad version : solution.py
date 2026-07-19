# Promblem - first bad version 
# Approach - binary search 
# Time and space complexity - 0(log n) & 0(1)
# Leetcode and diffculty level - 278 & easy 
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long long left = 1;
        long long right = n;

        int ans = n;

        while(left <= right) {

            long long mid = left + (right - left) / 2;

            if(isBadVersion(mid)) {
                ans = mid;
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return ans;
    }
};
