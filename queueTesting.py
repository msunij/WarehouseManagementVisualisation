# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 21:44:10 2018

@author: msunij
"""

import queue
import threading
import time

def doJob(que):#generic
    while True:
        item = que.get()
        job(item)
        que.task_done()
        
q = queue.Queue(maxsize=0)

def job(num):#job starting from finding closeset to deliver
    print(num*2)
    time.sleep(3)
    
    
for i in range(10):#excel item dict
    q.put(i)

numThread = 3#robot count
for i in range(numThread):
    thrd = threading.Thread(target=doJob,args=(q,))
    thrd.setDaemon(True)
    thrd.start()