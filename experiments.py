import random
import time
from main import MyMemoryManager # I import my own manager class from main.py

# Student Name: Nisa Nur Çavdar
# Student Number: B2380.011003
# This file runs all experiments (1, 2, and 3) that I explained in my report.

# --- EXPERIMENT 1: ALLOCATION TRACE ---
# In this part, I follow the trace sequence from the homework.
# I test Best Fit, Worst Fit, and Next Fit one by one.
def run_experiment_1_trace(test_mode):
    print(f"\n*** RUNNING EXPERIMENT 1: {test_mode.upper()} FIT ***")
    # This is the sequence: positive numbers mean allocate, negative means free.
    trace_sequence = [10, 5, 20, -5, 12, -10, 8, 6, 7, 3, 10]
    manager = MyMemoryManager(100)
    allocated_map = {} 

    for val in trace_sequence:
        if val > 0:
            # My logic for allocation
            addr = None
            if test_mode == 'best': addr = manager.allocate_best_fit(val)
            elif test_mode == 'worst': addr = manager.allocate_worst_fit(val)
            else: addr = manager.allocate_next_fit(val)

            if addr is not None:
                if val not in allocated_map: allocated_map[val] = []
                allocated_map[val].append(addr)
        else:
            # My logic for freeing memory
            size = abs(val)
            if size in allocated_map and allocated_map[size]:
                addr_to_free = allocated_map[size].pop(0)
                manager.free(addr_to_free, size)
        
        manager.print_status()

# --- EXPERIMENT 2: FRAGMENTATION TEST ---
# Here, I test how external fragmentation happens.
# I do 12 random jobs, then free 4, then try a big 25-unit request.
def run_experiment_2_frag(mode):
    print(f"\n*** RUNNING EXPERIMENT 2: {mode.upper()} FIT ***")
    mgr = MyMemoryManager(100)
    history = []

    # Step 1: 12 random allocations
    for _ in range(12):
        sz = random.randint(3, 12)
        if mode == 'best': addr = mgr.allocate_best_fit(sz)
        elif mode == 'worst': addr = mgr.allocate_worst_fit(sz)
        else: addr = mgr.allocate_next_fit(sz)
        if addr is not None: history.append((addr, sz))

    # Step 2: Free 4 blocks randomly
    if len(history) >= 4:
        for a, s in random.sample(history, 4):
            mgr.free(a, s)

    # Step 3: Try to find a 25-unit space
    print("\n[Final Check] Can I find 25 units of space?")
    if mode == 'best': res = mgr.allocate_best_fit(25)
    elif mode == 'worst': res = mgr.allocate_worst_fit(25)
    else: res = mgr.allocate_next_fit(25)

    if res is not None:
        print("RESULT: SUCCESS")
    else:
        print("RESULT: FAIL")
    mgr.print_status()

# --- EXPERIMENT 3: SPEED TEST ---
# I repeat 200 operations to see which algorithm is the fastest.
def run_experiment_3_speed():
    print("\n*** RUNNING EXPERIMENT 3: SPEED PERFORMANCE ***")
    for mode in ['best', 'worst', 'next']:
        mgr = MyMemoryManager(500)
        allocated_items = []
        start_time = time.perf_counter()
        
        for _ in range(200):
            size = random.randint(1, 10)
            if mode == 'best': addr = mgr.allocate_best_fit(size)
            elif mode == 'worst': addr = mgr.allocate_worst_fit(size)
            else: addr = mgr.allocate_next_fit(size)
            
            if addr is not None:
                allocated_items.append((addr, size))
            
            if allocated_items:
                idx = random.randint(0, len(allocated_items) - 1)
                a, s = allocated_items.pop(idx)
                mgr.free(a, s)
                
        end_time = time.perf_counter()
        print(f"{mode.upper()} total time: {end_time - start_time:.6f} seconds")

# This is the main part that runs everything
if __name__ == "__main__":
    # Experiment 1
    run_experiment_1_trace('best')
    run_experiment_1_trace('worst')
    run_experiment_1_trace('next')

    # Experiment 2
    run_experiment_2_frag('best')
    run_experiment_2_frag('worst')
    run_experiment_2_frag('next')

    # Experiment 3
    run_experiment_3_speed()
