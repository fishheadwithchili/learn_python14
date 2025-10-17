"""
场景 8：并发调试

应用：多线程或异步代码中追踪执行流
"""

import threading
import time

print("=" * 60)
print("多线程调试")
print("=" * 60)

def worker(task_id, duration):
    """工作线程"""
    thread_name = threading.current_thread().name
    thread_id = threading.get_ident()
    
    print(f"[开始] {task_id=}, {thread_name=}, {thread_id=}")
    time.sleep(duration)
    print(f"[完成] {task_id=}, 耗时={duration}s")

print("\n启动多个线程：\n")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i, 0.1), name=f"Worker-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n💡 总结：快速识别线程和任务对应关系")

