# -*- coding:utf-8 -*-
#Author:chao Yan

hset info name alex
hset info age 22
hset info id 3434
#get所有信息
hgetall info
#get具体的name字段
hget info name
#查看info这个hash中有多少个key
hkeys info
#查看info这个hash中有多少个value
hvals info
#批量插入和查询
hmset("info",{"name":"alex","age":22,"id":3232})
hmset info k1 1 k2 2
hmget info k1 k2
#获取有几个key
hlen info
#判断是否存在key
hexists info2 k3
#指定key自增长
hincrby info k2 1
#hscan过滤 如果info下的key特别多，全获取出来太费性能,匹配info中匹配k*的key的key和value
hscan info 0 match k*
#如果过滤后还是大，hscan_iter取 他是一个迭代器，不会影响到性能
for item in r.hscan_iter("xxx")







