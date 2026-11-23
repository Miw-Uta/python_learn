import threading
import time
import os

def coding(num):
    for i in range(num):
        print("coding", os.getppid(),os.getpid())
        time.sleep(0.2)

def music(count):
    for i in range(count):
        print("music", os.getppid(),os.getpid())
        time.sleep(0.2)

# 创建线程
coding_thread = threading.Thread(target=coding, args=(3,))
music_thread = threading.Thread(target=music, kwargs={"count": 3})


if __name__ == "__main__":
    # 启动线程
    coding_thread.start()
    music_thread.start()
