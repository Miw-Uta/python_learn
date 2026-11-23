import threading

# 全局变量
g_num = 0

# 创建互斥锁
mutex = threading.Lock()


def add_num1():
    # 加锁
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num = g_num + 1
    # 释放锁, 若不释放锁，其他线程将无法获取锁，导致死锁
    mutex.release()
    print(f"add_num1 : {g_num}")

def add_num2():
    # 加锁
    mutex.acquire()
    for i in range(1000000):
        global g_num
        g_num = g_num + 1
    # 释放锁
    mutex.release()
    print(f"add_num2 : {g_num}")

if __name__ == "__main__":
    # 创建线程
    add_thread1 = threading.Thread(target=add_num1)
    add_thread2 = threading.Thread(target=add_num2)

    # 启动线程
    add_thread1.start()
    add_thread2.start()
