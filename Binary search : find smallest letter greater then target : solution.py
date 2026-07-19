# Promblem - find smallest letter greater then target 
# Approach - binary search 
# Time and space complexity - 0(log n) & 0(n) 
# Leetcode and diffculty level - 744 & easy 
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int left = 0;
        int right = letters.size() - 1;

        while(left <= right) {

            int mid = left + (right - left) / 2;

            if(letters[mid] > target) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return letters[left % letters.size()];
    }  
};
