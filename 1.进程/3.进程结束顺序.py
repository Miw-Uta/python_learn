import multiprocessing
import time

def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)

if __name__ == "__main__":
    work_process = multiprocessing.Process(target = work)
    # 设置守护进程
    work_process.daemon = True
    # 设置后启动
    work_process.start()

    time.sleep(1)
    # 销毁子进程
    # work_process.terminate()
    print("主进程结束")
    