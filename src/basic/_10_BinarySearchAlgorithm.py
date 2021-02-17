

if __name__ == "__main__":
    #二分查找特性
    #1.必须单调递增或者递减
    #2.有上下边界
    #3.能通过index访问
    #二分查找模板
    l=[1,1,3,4,4,7,7,7,8]
    
    target = 4
    left ,right = 0,len(l)-1
    while left <= right:
        #容易数组越界
        #mid = (left + right) // 2
        mid = left+(right- left) // 2
        if l[mid] == target:
            # break or return result
            pass
        elif l[mid] < target:
            left = mid + 1
        else:
            right = mid -1
