//
// Created by jamesfchen on 2022/8/16.
//

#ifndef ALGORITHMS_LIST_H
#define ALGORITHMS_LIST_H

#include <iostream>
#include <vector>
#include <list>
#include <string>

using namespace std;
//using IntVector = vector<int>;
//typedef vector<string> StringVector;

template<class T>
void println(std::vector<T> a) {
    std::cout << "a = { ";
    for (int n : a) {
        std::cout << n << ", ";
    }
    std::cout << "};\n";
}

template<class T>
void println(std::list<T> l) {
    std::cout << "l = { ";
    for (int n : l) {
        std::cout << n << ", ";
    }
    std::cout << "};\n";
}


struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

string joinStr(ListNode *node, string formatStr) {
    if (node != nullptr) {
        cout<< formatStr<<endl;
        return joinStr(node->next, formatStr + "->" + to_string(node->val));
    } else {
        return formatStr + "->None";
    }
}

void println(ListNode *l) {
    string s = joinStr(l->next, std::to_string(l->val));
    string  formatStr = "cjf";
    std::cout << formatStr + "->None" +std::to_string(1) << std::endl;
}

ListNode *create_listnode(const std::vector<int> &datas) {
    int size = datas.size();
    std::vector<ListNode *> listnodes(size);
    for (int i = 0; i < size; ++i) {
        cout << datas[i] << endl;
        ListNode node = ListNode(datas[i]);
        listnodes[i] = &node;
        if (i != 0) {
            listnodes[i - 1]->next = &node;
        }
    }
    if (listnodes.size() > 0) {
        return listnodes[0];
    } else {
        return nullptr;
    }
}

#endif //ALGORITHMS_LIST_H
