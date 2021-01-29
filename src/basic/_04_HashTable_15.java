import java.util.*;
import java.util.function.Consumer;

public class _04_HashTable_15 {
    public static class Solution {
        public List<int[]> threeSum(int[] nums) {
            if (nums.length < 3) {
                return null;
            }
            List<int[]> ret = new ArrayList<>();
            Set<Integer> s = new HashSet<>();
            for (int i = 0; i < nums.length; i++) {
                int e1 = nums[i];
                for (int j = 0; j < nums.length; j++) {
                    if (i == j) continue;
                    int e2 = nums[j];
                    int y = -(e1 + e2);
                    if (s.contains(y)) {
                        int a = Math.min(y, Math.min(e1, e2));
                        int b = Math.max(y, Math.max(e1, e2));
                        int[] l = {a, -(a + b), b};
                        if (!ret.contains(l)) {
                            ret.add(l);
                            continue;
                        }
                    }
                    s.add(e2);
                }
                s.clear();
            }
            return ret;
        }
    }

    public static void main(String[] args) {
        int[] a = {-1, 0, 1, 2, -1, -4};
        int[] b = {-1, 0, 1, 2, -1, -4};

        System.out.println(Arrays.equals(a, b));
        Solution s = new Solution();
        s.threeSum(a).forEach(new Consumer<int[]>() {
                                  @Override
                                  public void accept(int[] ints) {

                                      System.out.println(Arrays.toString(ints));
                                  }
                              }

        );
    }
}
