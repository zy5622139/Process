# coding=utf-8
'''
@author: ZhangYu

Created on 2017/7/20
'''
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([12, {"name": "yuan"}, 'hello'])
    response = conn.recv()
    print("response", response)
    conn.close()
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    parent_conn.send("儿子你好!")
    p.join()