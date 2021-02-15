'''
哈希树的变种
'''
import numbers
alphabet_size=256#asccII


class Node:
    def __init__(self):
        self.end_of_word='#'
        self.root = {}