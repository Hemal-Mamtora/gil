### About

1. Experiment to demonstrate python concurrency and parallelism.
2. Also demonstrates python's Global Interpreter Lock (GIL)

### RUN

```bash
$ python concurrency.py
```

### Sample output
```
single threaded execution:
cpu_heavy_function: 9.6495 seconds
io_heavy_function: 10.0385 seconds
multi threaded execution
cpu_heavy_function: 8.0159 seconds
io_heavy_function: 1.0063 seconds
multi process execution
cpu_heavy_function: 1.6688 seconds
io_heavy_function: 1.1188 seconds
```

### Theory

#### Concurrency vs Parellelism

[External Link - Concurrency vs Parallelism](https://medium.com/@itIsMadhavan/concurrency-vs-parallelism-a-brief-review-b337c8dac350)

#### Global Interpreter Lock Python

[External Link - Global Interpreter Lock](https://realpython.com/python-gil/)