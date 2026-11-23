import time
# 创建启动进程
import multiprocessing
# 获取进程编号
import os

def coding(num,name):
    # 获取进程编号
    print(f"coding 父进程 ：{os.getppid()}")
    print(f"coding process id: {os.getpid()}")
    for i in range(num):
        print("Coding", name)
        time.sleep(0.3)

def music(count,name):
    print(f"music 父进程 ：{os.getppid()}")
    print(f"music process id: {os.getpid()}")
    for i in range(count):
        print("music", name)
        time.sleep(0.3)

# 创建进程
coding_process = multiprocessing.Process(target=coding, args=(3,"miu"))
music_process = multiprocessing.Process(target=music, kwargs={"name": "Miw","count": 3})


if __name__ == "__main__":
    print(f"父进程 ：{os.getpid()}")
    # 启动进程
    coding_process.start()
    music_process.start()