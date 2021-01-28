import java.util.*;

/**
 * 703. 数据流中的第 K 大元素
 * 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
 * <p>
 * 请实现 KthLargest 类：
 * <p>
 * KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
 * int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
 * <p>
 * <p>
 * 示例：
 * <p>
 * 输入：
 * ["KthLargest", "add", "add", "add", "add", "add"]
 * [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
 * 输出：
 * [null, 4, 5, 5, 8, 8]
 * <p>
 * 解释：
 * KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
 * kthLargest.add(3);   // return 4
 * kthLargest.add(5);   // return 5
 * kthLargest.add(10);  // return 5
 * kthLargest.add(9);   // return 8
 * kthLargest.add(4);   // return 8
 * <p>
 * <p>
 * 提示：
 * 1 <= k <= 104
 * 0 <= nums.length <= 104
 * -104 <= nums[i] <= 104
 * -104 <= val <= 104
 * 最多调用 add 方法 104 次
 * 题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素
 */


class KthLargest {
    int k;
    PriorityQueue<Integer> q;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        //小顶堆
//        this.q = new PriorityQueue<Integer>(k);
        //大顶堆
        this.q = new PriorityQueue<>(k, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });
        for (int n : nums) {
            add(n);
        }
    }

    public int add(int val) {
        if (q.size() <k){
            q .offer(val);
        }else if (val >q.peek()){
            q.poll();
            q.offer(val);
        }
//        q.peek();
//        q.element();//抛异常
//
//        q.offer(1);
//        q.add(2);//抛异常
//        q.poll();
//        q.remove();//抛异常

        return q.peek();
    }


    public static void main(String[] args) {
        int[] nums = {4, 2, 5, 1, 3};
        KthLargest ks = new KthLargest(4, nums);
        System.out.println(Arrays.toString(ks.q.toArray()));
        System.out.println(ks.add(1));
        System.out.println(Arrays.toString(ks.q.toArray()));
        System.out.println(ks.add(4));
        System.out.println(Arrays.toString(ks.q.toArray()));
        System.out.println(ks.add(5));
        System.out.println(Arrays.toString(ks.q.toArray()));
        System.out.println(ks.add(6));
        System.out.println(Arrays.toString(ks.q.toArray()));
    }
}