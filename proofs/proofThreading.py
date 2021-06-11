import time
import threading

def quickFunction(i, name, seconds):
    time.sleep(seconds)
    print(f"{name}: {i}")

def quickMany(name, seconds, stopEvents):
    i = 0
    while not all([s.is_set() for s in stopEvents]):
        quickFunction(i, name, seconds)
        i += 1

def slowFunction(name, seconds, stopEvent):
    print(f"{name}: start")
    time.sleep(seconds)
    print(f"{name}: done")
    stopEvent.set()


def main():
    slows = [
        {"function": slowFunction, "args": ["slow0", 5]},
        {"function": slowFunction, "args": ["slow1", 10]},
        # {"function": slowFunction, "args": ["slow2", 15]},
        # {"function": slowFunction, "args": ["slow3", 20]},
    ]

    quicks = [
        {"function": quickMany, "args": ["quick0", 0.1]},
        {"function": quickMany, "args": ["quick1", 0.5]},
        {"function": quickMany, "args": ["quick2", 1.0]},
    ]

    stopEvents = [threading.Event() for _ in slows]
    slowThreads = [threading.Thread(
        target=s["function"], 
        args=s["args"]+[stopEvents[i]]
    ) for i, s in enumerate(slows)]

    quickThreads = [threading.Thread(
        target=s["function"], 
        args=s["args"]+[stopEvents]
    ) for _, s in enumerate(quicks)]


    for th in quickThreads + slowThreads:
        th.daemon = True
        th.start()

    for th in quickThreads + slowThreads:
        th.join()

    print("finished")
    time.sleep(5)

if __name__ == "__main__":
    main()