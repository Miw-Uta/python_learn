import threading

# 全局变量
g_num = 0

def add_num1():
    for i in range(1000000):
        global g_num
        g_num = g_num + 1
    print(f"add_num1 : {g_num}")

def add_num2():
    for i in range(1000000):
        global g_num
        g_num = g_num + 1
    print(f"add_num2 : {g_num}")

if __name__ == "__main__":
    # 创建线程
    add_thread1 = threading.Thread(target=add_num1)
    add_thread2 = threading.Thread(target=add_num2)

    # 启动线程
    add_thread1.start()
    add_thread2.start()
