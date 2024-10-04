import threading
import time
import random

class Process:
    def __init__(self, id, total_processes):
        self.id = id
        self.total_processes = total_processes
        self.timestamp = 0
        self.requested = False
        self.reply_count = 0
        self.lock = threading.Lock()
        self.request_limit = 3  # Limit the number of requests per process
        self.request_count = 0  # Count how many requests have been made

    def request_critical_section(self):
        if self.request_count < self.request_limit:
            # Increment the timestamp
            self.timestamp += 1
            self.requested = True

            # Send request to all other processes
            print(f"Process {self.id} requesting critical section at timestamp {self.timestamp}.")
            for i in range(self.total_processes):
                if i != self.id:
                    processes[i].receive_request(self.id, self.timestamp)

            # Wait for replies from all other processes
            while self.reply_count < self.total_processes - 1:
                time.sleep(0.1)

            self.enter_critical_section()
            self.request_count += 1  # Increment the request count
        else:
            print(f"Process {self.id} has reached its request limit and will terminate.")

    def receive_request(self, sender_id, sender_timestamp):
        # Respond to request
        with self.lock:
            if self.requested and self.timestamp < sender_timestamp:
                # Queue the request if already in critical section or requested
                print(f"Process {self.id} queuing request from Process {sender_id} at timestamp {sender_timestamp}.")
                return
            else:
                # Send reply
                print(f"Process {self.id} sending reply to Process {sender_id}.")
                processes[sender_id].receive_reply(self.id)

    def receive_reply(self, sender_id):
        with self.lock:
            self.reply_count += 1
            print(f"Process {self.id} received reply from Process {sender_id}.")

    def enter_critical_section(self):
        print(f"Process {self.id} entering critical section.")
        time.sleep(random.uniform(1, 3))  # Simulate work in critical section
        print(f"Process {self.id} exiting critical section.")

        # Release the critical section
        self.release_critical_section()

    def release_critical_section(self):
        self.requested = False
        self.reply_count = 0
        print(f"Process {self.id} released critical section.")

def process_runner(process):
    while process.request_count < process.request_limit:
        # Simulate some work
        time.sleep(random.uniform(1, 2))
        process.request_critical_section()

# Number of processes
num_processes = 5
processes = [Process(i, num_processes) for i in range(num_processes)]

# Create threads for each process
threads = []
for process in processes:
    t = threading.Thread(target=process_runner, args=(process,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("All processes have completed their requests.")