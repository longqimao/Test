#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/12/16 9:42
from random import randint
def guess(start, end, maxTimes):
    # 生成一个区间为(start,end)的随机数
    value = randint(start, end)
    # 最大尝试次数
    maxTimes = maxTimes
    time = 0
    for i in range(maxTimes):
        time += 1
        prompt = 'Start to guess:' if i == 0 else 'Guess again:'
        # 添加异常处理，防止输入的不是数字
        try:
            x = int(input(prompt))
            if x == value:
                print('Congratulation!')
                print('你总共猜了', time, '次。')
                break
            elif x > value:
                print('Too big!')
            elif x < value:
                print('Too little!')
        except ValueError:
            print('Must input a number!')
    else:
        print('The value is', value)
guess(1, 10, 5)
