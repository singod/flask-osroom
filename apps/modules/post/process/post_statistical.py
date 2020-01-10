#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time : 2017/11/1 ~ 2019/9/1
# @Author : Allen Woo
from bson import ObjectId
from flask import request
from apps.utils.osr_async.osr_async import async_process
from apps.app import mdbs


@async_process()
def post_pv(post_id):
    """
    记录post的访问量
    :return:
    """
    mdbs["web"].init_app(reinit=True)
    sid = request.cookies["session"]
    r = mdbs["web"].db.access_record.find_one({"post_id": post_id, "sids": sid})
    if not r:
        mdbs["web"].db.access_record.update_one({"post_id": post_id},
                                            {"$inc": {"pv": 1}, "$addToSet": {"sids": sid}},
                                            upsert=True)
        mdbs["web"].db.post.update_one({"_id": ObjectId(post_id)},
                                   {"$inc": {"pv": 1}})
    else:
        if len(r["sids"]) > 1000:
            mdbs["web"].db.access_record.update_one({"post_id": post_id},
                                                {"$set": {"sids": []}})
