# -*- coding:utf-8 -*-
#Author:chao Yan

lpush names alex hanyan zhangyang
#取所有，先入后出
lrange names 0 -1
#先入先出
rpush names alex hanyan
#查看列表长度
llen(names)
#test插入alex之前
linsert names before（after） alex test

#修改
lset names 3 Alex

#删除 后入队列的
lpop names
rpop names

#只保留下角标1-2的数据
ltrim names 1 2


#如果有往names队列中写数据,数据会被消费到names2队列中,而names会是空队列,40为超时时间
brpoplpush names names2 40


#####集合

#集合会去重，只会插入3个值
#集合是无序的
sadd names3 alex alex jack jack 33
#获取值
smembers name3
#获取集合中元素的个数
scard(name3)
#在第一个集合中且不存在于第二个集合
sdiff name3 name4
#n6存储在name3集合中且不存在于name4集合中的数据
sdiffstore n6 name3 name4
#获取2个集合的交集
sinter name3 name4
#把1从name3集合移动到name4集合
smove name3 name4 1
#spop从集合尾部移除一个成员
spop name3
#从集合中随机获取1条数据,2代表2条数据
srandmember name3 2
#删除指定的值
srem names alex
#把两个集合合并
sunion name3 name4

#从集合开头匹配j开头的数据
sscan name3 0 match j*


#####有序集合
#添加数据的时候，添加权重
zadd name3 10 alex 5 jack
#获取值的顺序是得分从小到大
zrange names 0 -1
#带着分数
zrange names 0 -1 withscores
#获取集合中元素的数量
zcard(name3)
#获取集合中在分数范围的数据
zcount(name3,10,50)
#看下指定数据在集合中的排名
zrank name3 alex
#删除
zrem name3 alex
#删除排行在什么范围内的数据
zrenrangebyrank name3 0 4
#删除得分在什么范围内的数据
zremrangebyscore(name3,10,50)
#获取数据对应的分数
score name3 alex
#两个集合合并 并且把相同数据的得分做计算
zinterstore name 新集合 要合并几个集合 z1 z2

















