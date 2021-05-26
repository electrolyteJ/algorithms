package mock

import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import java.util.*
import kotlin.Comparator

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

//    println(g.take(1).toList())
//    println(g.take(1).toList())
//    println(g.take(4).toList())
    println("abd".compareTo("abc "))
    Collections.sort(nums.toList(),object : java.util.Comparator<Int> {
        override fun compare(o1: Int, o2: Int): Int {
            println("$o1,$o2")
            return when {
                o1> o2 -> {
                    1 // o1大于o2
                }
                o1< o2 -> {
                    -1
                }
                else -> {
                    0//表示两数相等
                }
            }
        }
    })

}
