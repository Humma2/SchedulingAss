total = int(raw_input("Enter a count of process :"))
time_slice = int(raw_input("Time Slice"))
for index in xrange(int(total)):
    p.append([])
    p[index].append(raw_input("Process:"))
    p[index].append(int(raw_input("Arrival Time:")))
    p[index].append(int(raw_input("Burst Time:")))

run = []
p.sort(key=lambda p: p[1])
tb = 0
import Queue
ready = Queue
arr = 0
ready.put(p[arr])
arr =arr+ 1
while not ready.empty():
     if run[2] >= time_slice:
        run[2] = run[2] - time_slice
        print run