if __name__ == "__main__":
    #二分查找特性
    #1.必须单调递增或者递减
    #2.有上下边界
    #3.能通过index访问
    #二分查找模板
    l = [1, 1, 3, 4, 4, 7, 7, 7, 8]

    target = 4
    left, right = 0, len(l) - 1
    #如果left <= right那么mid可以不算进去，不然容易形成死循环；如果left < right则一定要将mid算进去
    while left <= right:
        #如果left和right代表的是一个整数，就有必要使用后面一种写法防止整数越界
        #mid = (left + right) // 2
        mid = left + (right - left) // 2
        if l[mid] == target:
            # break or return result
            pass
        elif l[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
def bisect_left(a, x, lo=0, hi=None):
    '''
    如果目标值 等于 mid值，则取左边的区域,并且最后如果找到和目标值一样的值，则最insert到其left side
    '''
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo


def bisect_right(a, x, lo=0, hi=None):
    '''
    如果目标值 等于 mid值，则取右边的区域，并且最后如果找到和目标值一样的值，则最insert到其right side
    '''
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid+1
    return lo
