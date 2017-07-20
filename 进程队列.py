# coding=utf-8
'''
@author: ZhangYu

Created on 2017/7/20
'''
from multiprocessing import Process, Queue
import queue

def f(q,n):
    #q.put([123, 456, 'hello'])
    q.put(n*n+1)
    print("son process",id(q))

if __name__ == '__main__':
    q = Queue()  #try: q=queue.Queue()
    print("main process",id(q))

    for i in range(3):
        p = Process(target=f, args=(q,i))
        p.start()

    print(q.get())
    print(q.get())
    print(q.get())