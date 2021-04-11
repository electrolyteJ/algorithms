'''
x & 1 ==1 or 0奇偶性(x %2==1)
x = x&(x-1) 清零最低位的1
x & -x 得到最低位的1


位掩码(掩码：通过与目标数位运算屏蔽某些信息)的操作
user.premission | Update  添加新的信息
user.premission & Delete 检查存在某种信息
user.premission ^ Delete  获取另外一种信息
user.premission & ~ Insert 删除Insert信息
'''
