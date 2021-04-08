#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {

        int n = s.size();
        int m = p.size();

        // Set dp array
        bool dp[n+1][m+1];
        dp[0][0] = true;
        for (int i=1; i<n+1; i++) {
            dp[i][0] = false;
        }
        for (int j=1; j<m+1; j++) {
            dp[0][j] = false;
            if (p[j-1] == '*') {
                dp[0][j] = dp[0][j-2];
            }
        }

        // DP
        for (int i=1; i<n+1; i++) {
            for (int j=1; j<m+1; j++) {
                dp[i][j] = false;
                if (p[j-1] == '.' || s[i-1] == p[j-1]) {
                    dp[i][j] = dp[i-1][j-1];
                } else if (p[j-1] == '*') {
                    dp[i][j] = dp[i][j-2];
                    if (p[j-2] == '.' || p[j-2] == s[i-1]) {
                        dp[i][j] = dp[i][j] | dp[i-1][j];
                    }
                }
            }
        }

        // Print array
        cout << "    ";
        for (int j=0; j<m; j++) {
            cout << p[j] << " ";
        }
        cout << endl;
        for (int i=0; i<n+1; i++) {
            if (i>0) {
                cout << s[i-1] << " ";
            } else {
                cout << "  ";
            }
            for (int j=0; j<m+1; j++) {
                cout << dp[i][j] << " ";
            }
            cout << endl;
        }
        return dp[n][m];
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s = "aaaaaa";
    string p = ".*";
    Solution solution;
    cout << solution.isMatch(s, p) << endl;
    return 0;
}
