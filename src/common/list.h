//
// Created by jamesfchen on 2022/8/16.
//

#ifndef ALGORITHMS_LIST_H
#define ALGORITHMS_LIST_H

#include <iostream>
#include <list>
#include <string>
#include <vector>

using namespace std;
// using IntVector = vector<int>;
// typedef vector<string> StringVector;



struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


ListNode *create_listnode(const std::vector<int> &datas) {
    int size = datas.size();
    std::vector<ListNode *> listnodes(size);
    for (int i = 0; i < size; ++i) {
        //使用new之后还需要手动delete 不然就用智能指针
        auto *node = new ListNode(datas[i]);
        listnodes[i] = node;
        if (i != 0) {
            listnodes[i - 1]->next = node;
        }
    }
    if (listnodes.empty()) {
        return nullptr;
    } else {
        return listnodes[0];
    }
}

template<class T>
void print(const string &pre, std::vector<T> a) {
    cout << pre;
    std::cout << "a = { ";
    for (int n : a) {
        std::cout << n << ", ";
    }
    std::cout << "};\n";
}

template<class T>
void print(std::list<T> l) {
    std::cout << "l = { ";
    for (int n : l) {
        std::cout << n << ", ";
    }
    std::cout << "};\n";
}

string joinStr(ListNode *node, string formatStr) {
    if (node != nullptr) {
        return joinStr(node->next, formatStr + "->" + to_string(node->val));
    } else {
        return formatStr + "->nullptr";
    }
}

void print(const string &pre, ListNode *l) {
    cout << pre;
    if (l == nullptr) {
        cout << " nullptr" << endl;
        return;
    }
    string s = joinStr(l->next, std::to_string(l->val));
    cout << s << endl;
}

#endif // ALGORITHMS_LIST_H
