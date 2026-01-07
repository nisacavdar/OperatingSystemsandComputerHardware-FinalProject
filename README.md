# OperatingSystemsandComputerHardware-FinalProject 


**Student Name:** Nisa Nur Çavdar  
**Student ID:** B2380.011003  

## About My Project
In this project, I made a memory management simulation. I used **Linked List** for managing memory blocks. My code has three different algorithms:
1. **Best Fit:** It scans the list and finds the smallest hole for the request.
2. **Worst Fit:** It always picks the biggest hole in the memory.
3. **Next Fit:** It starts searching from the last position.

Also, my code has a **merge logic**. When I free a block, if there are neighbors, it combines them together. This is good for fragmentation.

## Project Structure
- `main.py`: This file has the main logic. My classes (`MyMemoryNode` and `MyMemoryManager`) and algorithms are here.
- `experiments.py`: This is my test script. It runs all 3 experiments (Trace, Fragmentation, and Speed) from my report.

## How to Run My Code
If you want to run my code and see the same results in my report, you can follow these:

1. You must have **Python** in your computer.
2. Download my files.
3. Open your terminal and go to the folder.
4. Write this command and press enter:
   ```bash
    python experiments.py
    ```
   
   
