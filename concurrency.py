import time
import threading
import multiprocessing as mp

def cpu_heavy_function(n = 600):
  for i in range(n):
    for j in range(n):
      i**j


def io_heavy_function():
  time.sleep(1)


def single_threaded_main(n = 10):
  print("single threaded execution:")

  start_time = time.time()
  for _ in range(n):
    cpu_heavy_function()
  end_time = time.time()
  print(f"cpu_heavy_function: {round(end_time - start_time, 4)} seconds")

  start_time = time.time()
  for _ in range(n):
    io_heavy_function()
  end_time = time.time()
  print(f"io_heavy_function: {round(end_time - start_time, 4)} seconds")


def multi_threaded_utility(function, function_name, n = 10):
  start_time = time.time()
  threads = []
  for _ in range(n):
    threads.append(threading.Thread(target=function))
  for t in threads:
    t.start()
  for t in threads:
    t.join()
  end_time = time.time()
  print(f"{function_name}: {round(end_time - start_time, 4)} seconds")
  

def multi_threaded_main():
  print("multi threaded execution")
  multi_threaded_utility(cpu_heavy_function, "cpu_heavy_function")
  multi_threaded_utility(io_heavy_function, "io_heavy_function")


def multiprocess_utility(function, function_name, n = 10):
  start_time = time.time()
  processes = []
  for _ in range(n):
    processes.append(mp.Process(target=function))
  for p in processes:
    p.start()
  for p in processes:
    p.join()
  end_time = time.time()
  print(f"{function_name}: {round(end_time - start_time, 4)} seconds")
  

def multiprocesss_main():
  print("multi process execution")
  multiprocess_utility(cpu_heavy_function, "cpu_heavy_function")
  multiprocess_utility(io_heavy_function, "io_heavy_function")


def main():
  single_threaded_main()
  multi_threaded_main()
  multiprocesss_main()

if __name__ == "__main__":
  main()

# TODO: vary the number of threads and processes
# TODO: explain the gap in single threaded cpu heavy vs multi threaded cpu heavy
