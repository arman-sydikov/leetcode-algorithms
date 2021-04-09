#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<int> pq;
        vector<int> v;
        for (auto p: lists) {
            while (p != nullptr) {
                pq.push(p->val);
                p = p->next;
            }
        }

        // print
        ListNode* root = nullptr;
        while (!pq.empty()) {
            root = new ListNode(pq.top(), root);
            pq.pop();
        }
        return root;
    }
};

int main() {
    vector<ListNode*> lists;
    {
        ListNode five(5);
        ListNode four(4, &five);
        ListNode one(1, &four);
        lists.push_back(&one);
    }
    {
        ListNode four(4);
        ListNode three(3, &four);
        ListNode one(1, &three);
        lists.push_back(&one);
    }
    {
        ListNode six(6);
        ListNode two(2, &six);
        lists.push_back(&two);
    }

    Solution solution;
    ListNode* root = solution.mergeKLists(lists);
    cout << root->val << endl;
}