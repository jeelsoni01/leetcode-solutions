class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;

    int i = 0;  // slow pointer: last unique position

    for (int j = 1; j < n; ++j) {  // fast pointer: scan array
        if (nums[j] != nums[i]) {  // found a new unique value
            ++i;
            nums[i] = nums[j];     // place it in the next unique slot
        }
    }

    // number of unique elements is i + 1
    return i + 1;   
    }
};