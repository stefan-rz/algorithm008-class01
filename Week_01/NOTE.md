# Array 实战题目

- [x] https://leetcode-cn.com/problems/container-with-most-water/

- [x] https://leetcode-cn.com/problems/move-zeroes/

- [x] https://leetcode.com/problems/climbing-stairs/

- [ ] [https://leetcode-cn.com/problems/3sum/ ](https://leetcode-cn.com/problems/3sum/)(高频老题）

  

#  Linked List 实战题目

- [ ] https://leetcode.com/problems/reverse-linked-list/

- [ ] https://leetcode.com/problems/swap-nodes-in-pairs

- [ ] https://leetcode.com/problems/linked-list-cycle

- [ ] https://leetcode.com/problems/linked-list-cycle-ii

- [ ] https://leetcode.com/problems/reverse-nodes-in-k-group/

  

#  课后作业

- [ ] https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
- [ ] https://leetcode-cn.com/problems/rotate-array/
- [ ] https://leetcode-cn.com/problems/merge-two-sorted-lists/
- [ ] https://leetcode-cn.com/problems/merge-sorted-array/
- [x] https://leetcode-cn.com/problems/two-sum/
- [x] https://leetcode-cn.com/problems/move-zeroes/
- [ ] https://leetcode-cn.com/problems/plus-one/



# 每日一题

- [ ] 04/13 https://leetcode-cn.com/problems/design-twitter/
- [ ] 04/15 https://leetcode-cn.com/problems/01-matrix/

刷题狂魔组

- [x] Day 1 https://leetcode-cn.com/problems/move-zeroes/
- [x] Day 2 https://leetcode-cn.com/problems/plus-one/
- [x] Day 3 https://leetcode-cn.com/problems/rotate-array/
- [x] Day 4 https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
- [x] Day 5  https://leetcode-cn.com/problems/squares-of-a-sorted-array/
- [ ] Additional  https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/
- [x] Day 6 https://leetcode-cn.com/problems/reverse-only-letters/
- [x] Day 7 https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/





# Week1 刷过的题 - 持续更新中

|                                                              |          |                                                              |                                                              |             |                            | 五毒神掌 |        |        |        |        |
  | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- | -------------------------- | -------- | ------ | ------ | ------ | ------ |
  | 题目                                                         | 数据结构 | 方法                                                         | 思路                                                         | 时间复杂度  | 空间复杂度                 | 第一遍   | 第二遍 | 第三遍 | 第四遍 | 第五遍 |
  | [1281. 整数的各位积和之差](https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) | 数学     | 提取位数                                                     | 1.模10得到当前为数<br />2. 除以10去掉当前为数<br />3.python 可以用divmod内置函数 | $O(log(N))$ | O(1)                       | 已刷     | 已刷   | 已刷   | 一周后 | 面试前 |
  | [189. 旋转数组](https://leetcode-cn.com/problems/rotate-array/) | 数组     | In-place 翻转                                                | Example：nums = [1,2,3,4,5,6,7] k = 3<br />Step1:划分成[1,2,3,4], [5,6,7]<br />Step2:分别reverse成这样，[4,3,2,1], [7,6,5]<br />Step3:合并且reverse，[5,6,7,1,2,3,4] | O(N)        | O(1)                       | 已刷     | 已刷   | 已刷   | 一周后 | 面试前 |
  | [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/) | 数组     | 同向双指针                                                   | 定义左右指针的物理意义左指针的左边区域都是非零数<br />- 右指针和左指针之间的区域都为零<br />- 右指针右边区域为探索区域 | O(N)        | O(1)                       | 已刷     | 已刷   | 已刷   | 一周后 | 面试前 |
  | [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/) | 数组     | 相向双指针                                                   | 题目就是要求2D的最大面积，所以无法同向，因为你不知道如何舍弃垂直线左右指针相向而行，计算出当前面积，然后进行判断<br />-如果左指针指向的垂直线较小，则移动左指针，反之则移动右指针<br />- 当前最大面积和新计算的面积打擂台，如果新的面积更大则更新最大面积 | O(N)        | O(1)                       | 刷       | 已刷   | 已刷   | 一周后 | 面试前 |
  | [15. 三数之和](https://leetcode-cn.com/problems/3sum/)       | 数组     | 相向双指针                                                   | 问题转化遍历数组，利用 2sum的双指针方法 找 target            | $O(N^2)$    | O(1)                       | 刷       | 已刷   | 已刷   | 一周后 | 面试前 |
  | [977. 有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/) | 数组     | 正常做法：双向双指针<br />tricky的做法（python独占)：直解计算平方值，然后sort，时间复杂度还是O(N) | 两左右指针，左指针指向的是负整数，右指针指向的是正整数<br /><br />循环出口：左指针指向了正整数， 或者右指针指向了负整数<br />判断条件是当左指针指向的当前负整数的平方大于右指针指向的当前正整数的平方，则把右指针指向平方指放入结果集，右子针往左移动，反之则左指针往右移动<br />根据循环跳出条件，我们需要后处理去处理那些没有来得及处理的整数，有点类似于merge 两个sorted 数组的后处理。 | O(N)        | O(N) - 开辟了N长度的结果集 | 刷       | 已刷   | 已刷   | 一周后 | 面试前 |
  | [面试题50. 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/) | 哈希表   | Python: dict/OrderedDict<br />Java: LinkedHashMap<br />开一个固定大小(128或者256 - ***ASCII***码作为数组的index | 遍历 数组一轮，存入哈希表，遍历哈希表一轮，找到第一个出现一次的字符 | $O(N)$      | O(N)                       | 刷       | 已刷   | 已刷   | 一周后 | 面试前 |
  |                                                              |          |                                                              |                                                              |             |                            |          |        |        |        |        |
  |                                                              |          |                                                              |                                                              |             |                            |          |        |        |        |        |
  |                                                              |          |                                                              |                                                              |             |                            |          |        |        |        |        |
  |                                                              |          |                                                              |                                                              |             |                            |          |        |        |        |        |
  |                                                              |          |                                                              |                                                              |             |                            |          |        |        |        |        |


# 数据结构

## 跳表

这里略，了解下就行了，因为没有具体题目，也就不多累赘了，留个参考资料方便后面想看的时候看看

## 有序字典

- python3.6后的字典建是有序的，而python3.6前则需要用`collections.OrderedDict()`
- 改进的地方在于利用一维数组做索引，不用再一次性的开8行3列的二维数组，内存消耗更低
- 因为有了索引，所以二维数组是按顺序的加入数值的

参考资料：

1. Redis - Skip List：[跳跃表](http://redisbook.readthedocs.io/en/latest/internal-datastruct/skiplist.html)、[为啥 Redis 使用跳表（Skip List）而不是使用 Red-Black？](http://www.zhihu.com/question/20202931)
2. [为什么Python 3.6以后字典有序并且效率更高？](https://www.cnblogs.com/xieqiankun/p/python_dict.html)
3. ASCII ([包括Java中2种表示ASCII的方式](https://blog.csdn.net/chy555chy/article/details/51938914))