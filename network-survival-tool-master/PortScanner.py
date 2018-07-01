import socket
import threading
import time
from queue import Queue

# print_lock prevents multiple threads from grabbing the same job. It is invoked in the functions below.
print_lock = threading.Lock()

# port_scan function loops through each port in range to find if it's open.
def port_scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            with print_lock:
                print("*"*20)
                print ("Port{}: Open" .format(port))
        sock.close()
    except:
        pass

# threader function gets a port from the queue, sets that port equal to worker.
# Then it puts the worker (i.e. port number) through the port_scan function.
def threader():
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()

# Start the program
if __name__=='__main__':

# It is very important to instantiate the Queue by setting it equal to some variable.
# If you don't, then the program won't run.
    q = Queue()

# These variables are required as inputs for port_scan function
# and also to set the range of ports that will be scanned.
    remoteServer = input("What is the domain of the target? ")
    remoteServerIP = socket.gethostbyname(remoteServer)
    scanstart = input("Scan starting at port #:")
    stopscan = input("to port #: ")

# Set the range, which means: how many threads do you want to run?
# Another way of saying this is: how many workers do you want working at the same time?
# Or, how many ports do you want to scan simultaneously? It's all the same.
# t.daemon means each worker dies with the main. They can't exist independently, if the main process has ended.
# t.start() starts the threader function.
    for x in range(100):
       t = threading.Thread(target=threader)
       t.daemon = True
       t.start()

# Grab the time you started scanning ports so you can measure performance
    start = time.time()

# Set the range of ports to be scanned.
# Each time a worker is q.put to worker a port number is fed into the port_scan function,
# Since 1 worker = 1 port
    for worker in range(int(scanstart), int(stopscan)):
        q.put(worker)

# Stop the threading
    q.join()

    print("\n")
    print('Scan time:',time.time() - start)