# coding=utf-8
'''
@author: ZhangYu

Created on 2017/7/20
'''
from multiprocessing import Process, Manager

def f(d, l,n):

    d[n] = n
    d["name"] ="alvin"
    l.append(n)

    #print("l",l)

if __name__ == '__main__':

    with Manager() as manager:

        d = manager.dict()

        l = manager.list(range(5))
        p_list = []

        for i in range(5):
            p = Process(target=f, args=(d,l,i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)