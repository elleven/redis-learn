# -*- coding:utf-8 -*-
#Author:chao Yan


import redis

pool = redis.ConnectionPool(host="",port=6379)

r=redis.Redis(connection_pool=pool)
r.set(name,value,ex=None,px=None,nx=False,xx=False)

ex:过期时间（s）
px:过期时间（毫秒）
nx:如果设置为True,则只有name不存在时,当前set操作才执行
xx:如果设置为True,则只有name存在时，当前的set操作才执行

#批量设置
mset(k1="v1",k2="v2")
mset({"k1":"v1","k2":"v2"})

#批量获取多个值
mget("a1","a2")
mget(["a1","a2"])

#设置新值并返回以前的值
getset("a1","b1")

#获取key对应值得字符截取,取第0位到第2位的值
getrange("a1",0,2)

#把key是a1的值得第0位换成|
setrange("a1",0,"|")
#从1这个位置往后直接覆盖
setrange("a1",1,"AL")

#把a转成二进制
#把a转成asci码
asci = ord("a")
#把asci码转成二进制
bin(asci)


#统计在线用户
setbit n5 1000 1
setbit n5 200 1
setbit n5 201 1
#统计在线用户个数设置为1的
bitcount n5
#查看用户id是55的是否在线
getbit n5 55

#获取字符串长度
strlen(key)

#给login_user这个key每次+1
incr login_users
#给login_users这个key每次-1
decr login_users

#append在值后面追加li
append key li





