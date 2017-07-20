# coding=utf-8
'''
@author: ZhangYu

Created on 2017/7/20
'''
from multiprocessing import Pool
import time

def foo(args):
 time.sleep(1)
 print(args)

if __name__ == '__main__':
 p = Pool(5)
 for i in range(30):
     p.apply_async(func=foo, args= (i,))

 p.close()   # 等子进程执行完毕后关闭线程池
 # time.sleep(2)
 # p.terminate()  # 立刻关闭线程池
 p.join()