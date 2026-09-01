class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> result;

        for (auto interval : intervals) {
            
            // No overlap
            if (result.empty() || result.back()[1] < interval[0]) {
                result.push_back(interval);
            }
            
            // Overlap
            else {
                result.back()[1] = max(result.back()[1], interval[1]);
            }
        }

        return result;
    }
};