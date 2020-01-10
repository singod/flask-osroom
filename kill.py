#!/usr/bin/env python3
# -*-coding:utf-8-*-
# @Time : 2017/11/1 ~ 2019/9/1
# @Author : Allen Woo
import os
try:
    shcmd = """ps -ef | grep uwsgi.ini | awk '{print $2}' | xargs kill -9"""
    r = os.system(shcmd)
    print("Kill uwsgi.")
except Exception as e:
    print(e)
