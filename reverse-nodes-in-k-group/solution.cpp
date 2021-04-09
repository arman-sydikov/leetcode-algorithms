#include <iostream>
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* h = head;
        ListNode* e = head;
        ListNode* last = nullptr;
        ListNode* p = head;
        ListNode* answer = nullptr;
        int nodes = 0;
        while (p) {
            nodes++;
            p = p->next;
            if (nodes == k) {
                while (--nodes) {
                    ListNode* temp = e->next;
                    e->next = temp->next;
                    temp->next = h;
                    h = temp;
                }
                if (answer == nullptr) {
                    answer = h;
                }
                if (last != nullptr) {
                    last->next = h;
                }
                last = e;
                h = p;
                e = p;
            }
        }
        if (answer == nullptr) {
            answer = head;
        }
        return answer;
    }
};

int main() {
    ListNode* five = new ListNode(5);
    ListNode* four = new ListNode(4, five);
    ListNode* three = new ListNode(3, four);
    ListNode* two = new ListNode(2, three);
    ListNode* one = new ListNode(1);
    int k = 1;
    Solution* solution = new Solution();
    ListNode* answer = solution->reverseKGroup(one, k);
    while (answer != nullptr) {
        cout << answer->val << endl;
        answer = answer->next;
    }
}