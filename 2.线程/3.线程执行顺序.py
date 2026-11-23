import threading
import time

# current_thread() 方法获取当前线程对象
def get_info():
    time.sleep(0.5)
    current_thread = threading.current_thread()
    print(current_thread)

if __name__ == "__main__":
    # 创建线程
    for i in range(10):
        sub_thread = threading.Thread(target=get_info)
        sub_thread.start()

   
