def insertion_sort(nums):
    '''
    平均时间复杂度O(n^2)
    '''
    pass


def shell_sort(nums):
    '''
    策略选择：希尔排序是插入排序的一种高效率的实现
    平均时间复杂度O(n^1.3)
    '''
    pass


def selection_sort(nums):
    '''
    优化了冒泡排序，是其改良版。
    平均时间复杂度O(n^2)
    '''
    pass


def heap_sort(nums):
    '''
    策略选择：借助堆来实现，思想同简单的选择排序
    平均时间复杂度O(nlogn)
    '''
    pass


def bubble_sort(nums):
    '''
    - 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
    - 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
    - 针对所有的元素重复以上的步骤，除了最后一个；
    - 重复步骤1~3，直到排序完成。
    平均时间复杂度O(n^2)
    '''
    for i in range(len(nums)):
        for j in range(len(nums) - i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


def quick_sort(nums):
    '''
    总结快速排序的思想：冒泡+二分+递归分治
    - 从数列中挑出一个元素，称为 “基准”（pivot）；
    - 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该 基准就处于数列的中间位置。这个称为分区（partition）操作；
    - 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
    平均时间复杂度O(nlogn) 空间复杂度O(nlogn)
    '''
    def partition(nums, l, r):
        # pivot = nums[r]
        # i = l-1
        # for j in range(l,r):
        #     if nums[j]<pivot:#比pivot小的数多排到左边
        #         i +=1
        #         nums[i],nums[j] = nums[j],nums[i]
        # i +=1
        # nums[i],nums[r]=nums[r],nums[i]
        pivot = nums[l]
        i, j = l, r
        while i < j:
            '''
            通过双指针，一个找出大于pivot的数，一个找出小于pivot的数，然后通过交换把大的放在右边，小的放在左边
            '''
            while i < j and nums[j] >= pivot:#找出比pivot小的数，然后把大的数都放在右边
                j -= 1
            while i < j and nums[i] <= pivot:#找出比pivot大的数，然后通过交换，把大的数放在右边
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[l] = nums[l], nums[i]
        return i

    def quick_sort_inner(nums, l, r):
        if l >= r:
            return
        pivot_i = partition(nums, l, r)
        quick_sort_inner(nums, l, pivot_i - 1)
        quick_sort_inner(nums, pivot_i + 1, r)

    quick_sort_inner(nums, 0, len(nums)-1)


def merge_sort(nums):
    '''
    divide-conquer
    平均时间复杂度O(nlogn) 空间复杂度O(n)
    '''
    if not nums:
        return

    def merge(nums, l, mid, r):
        p1, p2 = l, mid+1
        for i in range(l, r+1):
            b[i] = nums[i]
        for i in range(l, r+1):
            if p1 > mid:  # 左边的数据已经compare完，就直接把右边数据copy到数组
                nums[i] = b[p2]
                p2 += 1
            elif p2 > r:  # 直接把左边数据copy到数组
                nums[i] = b[p1]
                p1 += 1
            elif b[p2] < b[p1]:  # 比较左边数据和右边数组头一个
                nums[i] = b[p2]
                p2 += 1
            else:
                nums[i] = b[p1]
                p1 += 1

    def merge_sort_inner(nums, l, r):
        if l >= r:
            return
        mid = l+(r-l)//2  # (r+l)//2
        merge_sort_inner(nums, l, mid)
        merge_sort_inner(nums, mid+1, r)
        merge(nums, l, mid, r)

    b = [0]*len(nums)
    merge_sort_inner(nums, 0, len(nums)-1)


def counting_sort(nums):
    '''
    平均时间复杂度O(n+k)
    '''
    pass


def bucket_sort(nums):
    '''
    平均时间复杂度O(n+k)
    '''
    pass


def radix_sort(nums):
    '''
    平均时间复杂度O(n*k)
    '''
    pass


if __name__ == '__main__':
    nums = [12, 3, 7, 8, 4, 2, 7, 4, 29]
    # insertion_sort(nums)
    # print('1 insertion_sort',nums)
    # shell_sort(nums)
    # print('2 shell_sort',nums)
    # selection_sort(nums)
    # print('3 selection_sort', nums)
    # heap_sort(nums)
    # print('4 heap_sort', nums)
    bubble_sort(nums)
    print('5 bubble_sort', nums)
    nums = [12, 3, 7, 8, 4, 2, 7, 4, 29]
    quick_sort(nums)
    print('6 quick_sort', nums)
    nums = [12, 3, 7, 8, 4, 2, 7, 4, 29]
    merge_sort(nums)
    print('7 merge_sort', nums)
    # counting_sort(nums)
    # print('8 counting_sort',nums)
    # bucket_sort(nums)
    # print('9 bucket_sort',nums)
    # radix_sort(nums)
    # print('10 radix_sort', nums)
