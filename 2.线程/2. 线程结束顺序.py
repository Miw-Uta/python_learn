import threading
import time
import os

def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)

if __name__ == "__main__":
    # 创建线程
    # 方式一： 参数设置守护主线程
    # work_thread = threading.Thread(target=work, daemon=True)
    work_thread = threading.Thread(target=work)
    # 启动线程
    # 方式二
    work_thread.setDaemon(True)
    work_thread.start()
    # 主线程继续执行
    time.sleep(1)
    print("主线程结束")