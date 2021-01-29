package mock

import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch

fun gen(nums: IntArray) = sequence {
    for (i in 0 until nums.size) {
        yield(nums[i])
    }
}

fun main() {
    GlobalScope.launch {


    }
    val nums = intArrayOf(1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6)
    val g = gen(nums)

    println(g.take(1).toList())
    println(g.take(1).toList())
    println(g.take(4).toList())

}
