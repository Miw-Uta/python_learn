import time
import multiprocessing

ls = []

def write():
    for i in range(3):
        ls.append(i)
        print(f"add {i}")
    print(f"write : {ls}")

def read():
    print(f"read : {ls}")

if __name__ == "__main__":
    write_process = multiprocessing.Process(target=write)
    read_process = multiprocessing.Process(target=read)

    write_process.start()
    write_process.join()  # 等待写入进程结束后再执行读取
    time.sleep(1)  # 确保写入完成后再读取
    read_process.start()