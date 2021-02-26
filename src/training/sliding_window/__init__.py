#滑动窗口模板
def sliding_window(s):
    import collections
    left,right=0,0
    counter,max_len=0,0
    lookup = collections.defaultdict(int)
    while right < len(s):
        if lookup[s[right]] > 0 :
            counter +=1
        lookup[s[right]] +=1
        right +=1
        while counter > 0:
            if lookup[s[left]] > 1:
                counter -=1
            lookup[s[left]] -=1
            left +=1
        max_len = max(max_len,right - left)
    return max_len

if __name__ == '__main__':
    pass
    
