# Promblem - koko eating bananas 
# Appraoch - binary search 
# Time and space complexity - 0(n log(maxPile)) & 0(1) 
# Leetcode and diffculty level - 875 & medium 
class Solution {
public:
    bool canEat(vector<int>& piles , int h, int speed) {
        int hours = 0;

        for(int bananas : piles) {
            hours += (bananas + speed - 1) / speed;
        }
        return hours<=h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *max_element(piles.begin(), piles.end());
        int ans = right;

        while(left <= right) {
            int mid = left + (right - left) / 2;
            if(canEat(piles,h,mid)) {
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
