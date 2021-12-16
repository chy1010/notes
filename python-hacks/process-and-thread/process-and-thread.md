# Program, Process, and Thread

- links:
    * https://totoroliu.medium.com/program-process-thread-%E5%B7%AE%E7%95%B0-4a360c7345e5
    * https://oldmo860617.medium.com/%E9%80%B2%E7%A8%8B-%E7%B7%9A%E7%A8%8B-%E5%8D%94%E7%A8%8B-%E5%82%BB%E5%82%BB%E5%88%86%E5%BE%97%E6%B8%85%E6%A5%9A-a09b95bd68dd


- program (程式)
    - code, not loaded in memory
- process (程序, 進程)
    - program which is loaded in memory
    - may see processes in mac on the activity monitor (活動監視器) / process viewer.

- thread (執行緒, 線程)
    - the segment of a process
    - a process can have multiple threads
    - these threads are contained within a process
    - a thread has 3 states: running, ready, and blocked.
    - threads within the same process shares the memory and variables

## multi-processing and multi-threading

- multi-processing with one thread:
    * finish more task in the same time
- multi-threading in a process:
    * same task done in shorter time
    * multi-threading: different threads share the same memory and variables, may cause deadlock.

### concurrent v.s. parallel

- parallel:
    * do parallel tasks by serveral cpus
- concurrent:
    * all tasks are done by the same one cpu
    * one time one task is executed


# Coroutine (協程)?

- to be continued