import threading
import time

def runner(name, count):
    """ Thread running function. """

    for i in range(count):
        print(f"Running: {name} {i}")
        time.sleep(0.2)  # seconds

# Launch this many threads
THREAD_COUNT = 10

# We need to keep track of them so that we can join() them later. We'll
# put all the thread references into this array
threads = []
result = [0] * THREAD_COUNT
ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16],
    [7, 11],
    [3, 7],
    [121, 122],
    [1, 10],
    [9, 12]
]
# Launch all threads!!
for i in range(THREAD_COUNT):
    # Give them a name
    name = f"Thread{i}"

    start = ranges[i][0]
    end = ranges[i][1]
    result[i] = sum(range(start, end)) + end

    # Set up the thread object. We're going to run the function called
    # "runner" and pass it two arguments: the thread's name and count:
    t = threading.Thread(target=runner, args=(name, i + THREAD_COUNT))

    # The thread won't start executing until we call `start()`:
    t.start()

    # Keep track of this thread so we can join() it later.
    threads.append(t)

# Join all the threads back up to this, the main thread. The main thread
# will block on the join() call until the thread is complete. If the
# thread is already complete, the join() returns immediately.

for t in threads:
    t.join()

print(result)
print(sum(result))