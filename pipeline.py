# -*- coding:utf-8 -*-
#Author:chao Yan

import redis

pool = redis.ConnectionPool(host='',port=)
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

r.set("name","alex")
r.set("name1","alex1")

pipe.execute()
