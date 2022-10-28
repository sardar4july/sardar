import os
import threading
import time

def task_sleep(sleep_dur,task_no,lock):
    lock.acquire()
    time.sleep(sleep_dur)
    lock.release()

    print(f"task {task_no}done (slept for {sleep_dur}s)",
          f"Main thread : {threading.main_thread().name}",
          f"current thread : {threading.current_thread().name}",
          f"Process ID:{os.getpid()}")

if __name__=="__main__" :
    time_start=time.time()
    thread_lock=threading.Lock()
    t1=threading.Thread(target=task_sleep,args=(2,1,thread_lock))
    t2=threading.Thread(target=task_sleep,args=(2,2,thread_lock))
    t1.start()
    time1_start = time.time()
    t2.start()
    end2_start = time.time()

    t1.join()
    t2.join()

    time_end=time.time()
    print(f"time elapsed :{round(time_end-time_start,2)}s")

