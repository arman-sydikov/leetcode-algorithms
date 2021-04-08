#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& top, vector<int>& bottom) {
        if (top.size() > bottom.size()) {
            return findMedianSortedArrays(bottom, top);
        }
        int left = 0;
        int right = top.size();
        double answer;
        while (left<=right) {

            // Calculate top and bottom middles
            int topMiddle = (left+right)/2;
            int bottomMiddle = (top.size()+bottom.size()+1)/2 - topMiddle;

            // Set top left and right
            int topLeft = INT_MIN;
            int topRight = INT_MAX;
            if (topMiddle > 0 ) {
                topLeft = top[topMiddle-1];
            }
            if (topMiddle < top.size()) {
                topRight = top[topMiddle];
            }

            // Set bottom left and right
            int bottomLeft = INT_MIN;
            int bottomRight = INT_MAX;
            if (bottomMiddle > 0) {
                bottomLeft = bottom[bottomMiddle-1];
            }
            if (bottomMiddle < bottom.size()) {
                bottomRight = bottom[bottomMiddle];
            }

            // Binary search
            if (bottomLeft > topRight) {
                left = topMiddle+1;
                continue;
            }
            if (topLeft > bottomRight) {
                right = topMiddle-1;
                continue;
            }

            // Found 
            if ((top.size()+bottom.size())%2==0) {
                answer = ((double) max(topLeft, bottomLeft) + min(topRight, bottomRight))/2;
            } else {
                answer = max(topLeft, bottomLeft);
            }
            break;
        }
        return answer;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
  
#ifndef ONLINE_JUDGE
    // freopen("input.txt", "r", stdin);
    // freopen("error.txt", "w", stderr);
    // freopen("output.txt", "w", stdout);
#endif

    vector<int> nums1{1,1,1,1,1,1,1,1,1,1,4,4};
    vector<int> nums2{1,3,4,4,4,4,4,4,4,4,4};
    Solution s;
    cout << s.findMedianSortedArrays(nums1, nums2) << endl;
    return 0;
}
