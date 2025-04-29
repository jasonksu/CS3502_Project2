import queue
import random

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.start_time = None
        self.finish_time = None

def shortest_remaining_time_first(process_list):
    time = 0
    completed = []
    ready_queue = []
    gantt_chart = []

    while process_list or ready_queue:
        # Add processes that have arrived
        while process_list and process_list[0].arrival_time <= time:
            ready_queue.append(process_list.pop(0))

        # Select process with shortest remaining time
        if ready_queue:
            ready_queue.sort(key=lambda x: x.remaining_time)
            current = ready_queue.pop(0)

            if current.start_time is None:
                current.start_time = time

            gantt_chart.append(current.pid)

            time += 1
            current.remaining_time -= 1

            if current.remaining_time == 0:
                current.finish_time = time
                completed.append(current)
            else:
                ready_queue.append(current)
        else:
            gantt_chart.append('Idle')
            time += 1

    return completed, gantt_chart

def multilevel_feedback_queue(process_list):
    time = 0
    completed = []
    queues = [queue.Queue(), queue.Queue(), queue.Queue()]
    time_quantums = [4, 8, 12]  # Example time quantums

    gantt_chart = []

    while process_list or any(not q.empty() for q in queues):
        # Add newly arrived processes to the highest priority queue
        while process_list and process_list[0].arrival_time <= time:
            queues[0].put(process_list.pop(0))

        executed = False
        for i in range(len(queues)):
            if not queues[i].empty():
                current = queues[i].get()

                if current.start_time is None:
                    current.start_time = time

                tq = time_quantums[i]
                execution_time = min(current.remaining_time, tq)

                for _ in range(execution_time):
                    gantt_chart.append(current.pid)
                    time += 1

                    # Add any newly arriving processes during execution
                    while process_list and process_list[0].arrival_time <= time:
                        queues[0].put(process_list.pop(0))

                current.remaining_time -= execution_time

                if current.remaining_time == 0:
                    current.finish_time = time
                    completed.append(current)
                else:
                    # Move to lower queue if not finished
                    if i < 2:
                        queues[i+1].put(current)
                    else:
                        queues[i].put(current)
                executed = True
                break

        if not executed:
            gantt_chart.append('Idle')
            time += 1

    return completed, gantt_chart

def calculate_metrics(completed_processes, total_time):
    n = len(completed_processes)
    total_waiting = sum((p.finish_time - p.arrival_time - p.burst_time) for p in completed_processes)
    total_turnaround = sum((p.finish_time - p.arrival_time) for p in completed_processes)

    awt = total_waiting / n
    att = total_turnaround / n
    cpu_util = (sum(p.burst_time for p in completed_processes) / total_time) * 100
    throughput = n / total_time

    return awt, att, cpu_util, throughput

def print_gantt_chart(gantt_chart):
    print("\nGantt Chart:")
    for pid in gantt_chart:
        print(f"| {pid} ", end="")
    print("|\n")

def main():
    print("CPU Scheduling Simulation")
    print("1. Shortest Remaining Time First (SRTF)")
    print("2. Multi-Level Feedback Queue (MLFQ)")
    choice = int(input("Enter your choice (1 or 2): "))

    n = int(input("Enter number of processes: "))
    process_list = []
    for i in range(n):
        arrival = int(input(f"Enter arrival time for P{i}: "))
        burst = int(input(f"Enter burst time for P{i}: "))
        process_list.append(Process(f"P{i}", arrival, burst))

    # Sort by arrival time initially
    process_list.sort(key=lambda x: x.arrival_time)

    if choice == 1:
        completed, gantt_chart = shortest_remaining_time_first(process_list)
    elif choice == 2:
        completed, gantt_chart = multilevel_feedback_queue(process_list)
    else:
        print("Invalid choice.")
        return

    total_time = max(p.finish_time for p in completed)

    print_gantt_chart(gantt_chart)

    awt, att, cpu_util, throughput = calculate_metrics(completed, total_time)
    print(f"Average Waiting Time: {awt:.2f}")
    print(f"Average Turnaround Time: {att:.2f}")
    print(f"CPU Utilization: {cpu_util:.2f}%")
    print(f"Throughput: {throughput:.2f} processes/unit time")

if __name__ == "__main__":
    main()
