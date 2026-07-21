# Promblem - capacity to ship packages in d days 
# Approach - binary search 
# Time and space complexity - 0(n log(sum)) & 0(1)
# Leetcode and diffculty level - 1011 & medium 
class Solution {
public:
    bool canShip(vector<int>& weights, int days, int capacity) {
        int currentWeight = 0;
        int requiredDays = 1;

        for(int weight : weights) {
            if(currentWeight + weight <= capacity) {
                currentWeight += weight;
            }
            else {
                requiredDays++;
                currentWeight = weight;
            }
        }
        return requiredDays <= days;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int left = *max_element(weights.begin(), weights.end());
        int right = accumulate(weights.begin(),weights.end(),0);
        int ans = right;

        while(left <= right) {
            int mid = left + (right - left) / 2;

            if(canShip(weights,days,mid)) {
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
