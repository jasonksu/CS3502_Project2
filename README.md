# CPU Scheduler Project - CS3502

## Overview
This project is a CPU scheduling simulator that implements two scheduling algorithms from scratch:
- **Shortest Remaining Time First (SRTF)**
- **Multi-Level Feedback Queue (MLFQ)**

It was created for CS 3502 (Operating Systems) at Kennesaw State University as part of Project 2.  
The purpose of the project is to compare the performance of different CPU scheduling algorithms based on real scheduling metrics.

## Features
- **Shortest Remaining Time First (SRTF)**:  
  Picks the process with the least amount of remaining CPU time at every time unit.

- **Multi-Level Feedback Queue (MLFQ)**:  
  Uses multiple queues with different time quantums and dynamic priority adjustments.

- **Performance Metrics Calculated**:
  - Average Waiting Time (AWT)
  - Average Turnaround Time (ATT)
  - CPU Utilization (%)
  - Throughput (processes per unit time)

- **Gantt Chart** generation for visualizing the scheduling timeline.

- **User Input**:
  - Number of processes
  - Arrival time and burst time for each process
  - Selection between SRTF or MLFQ algorithm

## How to Run

1. Make sure you have **Python 3.x** installed on your system.

2. Clone or download this repository.

3. Open a terminal (Command Prompt) and navigate to the project folder.

4. Run the program with:

```bash
python cpu_scheduler.py

(If python doesn't work, try python3.)

Follow the on-screen prompts:

Choose scheduling algorithm (1 for SRTF, 2 for MLFQ).

Enter process details (arrival time and burst time).

The program will display the Gantt Chart and print all performance metrics after scheduling is completed.

Notes
This project was built entirely from scratch without using the provided starter GUI code.

The simulation runs in the console (text-based, no graphical interface).

Designed for cross-platform compatibility.
