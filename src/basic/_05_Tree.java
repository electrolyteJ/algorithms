import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.TreeSet;

/**
 * tree and binary search tree
 */
public class _05_Tree {
    public static void main(String[] args) {
        //java C++标准库树都是用红黑树
//        List<Integer> l = Arrays.asList(5, 1, 4, null, null, 3, 6);
        List<Integer> l = Arrays.asList(5, 1, 4, 3, 6);
        TreeSet<Integer> ts = new TreeSet<>(l);
        System.out.println(Arrays.toString(ts.toArray()));
//        System.out.println("tree first:"+ts.first()+" tree last:"+ts.last());
//        System.out.println(
//        ts.tailSet(5)
//        );
//        System.out.println(ts.headSet(5));
    }

//    public List<Integer> inorder(TreeSet<Integer> ts){
//        if (ts ==null) return Collections.emptyList();
//    }
}
