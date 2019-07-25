# -*- coding:utf-8 -*-
#Author:chao Yan

import redis

pool = redis.ConnectionPool(host="",port=6379)

r=redis.Redis(connection_pool=pool)
r.set("foo","bar")