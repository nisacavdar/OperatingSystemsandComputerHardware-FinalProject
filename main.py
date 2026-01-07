# Student Name:Nisa Nur Çavdar
# Student Number:B2380.011003
# Question 3: Memory Allocation Simulation
# I use a Linked List to manage 100 units of memory.

class MyMemoryNode:
    def __init__(self, start, length):
        self.start = start
        self.length = length
        self.next = None


class MyMemoryManager:
    def __init__(self, total_size=100):
        # In the beginning, we have one big free block: [0, 100]
        self.head = MyMemoryNode(0, total_size)
        # I use this for Next Fit to remember where I am
        self.next_fit_ptr = self.head

    # BEST FIT
    # My logic: I look at all blocks and pick the SMALLEST one that is enough.
    def allocate_best_fit(self, size):
        print(f"\n[Action] Best Fit Request: {size} units")
        best_choice = None
        current = self.head

        while current:
            if current.length >= size:
                # I want the smallest suitable block to save big ones
                if best_choice is None or current.length < best_choice.length:
                    best_choice = current
            current = current.next

        if best_choice:
            return self._split_and_update(best_choice, size)
        print("Result: FAIL - No space.")
        return None

    # WORST FIT
    # My logic: I scan and pick the BIGGEST block.
    def allocate_worst_fit(self, size):
        print(f"\n[Action] Worst Fit Request: {size} units")
        worst_choice = None
        current = self.head

        while current:
            if current.length >= size:
                # I pick the maximum space to keep leftover big
                if worst_choice is None or current.length > worst_choice.length:
                    worst_choice = current
            current = current.next

        if worst_choice:
            return self._split_and_update(worst_choice, size)
        print("Result: FAIL - No space.")
        return None

    # NEXT FIT
    # My logic: I don't start from zero. I start from my last position.
    def allocate_next_fit(self, size):
        print(f"\n[Action] Next Fit Request: {size} units")
        if not self.head: return None

        start_node = self.next_fit_ptr if self.next_fit_ptr else self.head
        current = start_node

        while True:
            if current.length >= size:
                # Update pointer to next for the next time
                self.next_fit_ptr = current.next
                return self._split_and_update(current, size)

            # If I reach end, I go back to start (circular search)
            current = current.next if current.next else self.head
            if current == start_node:
                break

        print("Result: FAIL - No space.")
        return None

    # I use this to split a block after I choose it
    def _split_and_update(self, node, size):
        start_addr = node.start
        if node.length == size:
            # If it is exact size, I remove it from the list
            self._remove_block(node)
        else:
            # If there is leftover, I make the block smaller
            node.start += size
            node.length -= size
        return start_addr

    def _remove_block(self, target):
        if self.head == target:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next == target:
                curr.next = curr.next.next
                break
            curr = curr.next

    #  FREE AND MERGE
    # My logic: I put memory back and MERGE if they are neighbors.
    def free(self, start, size):
        print(f"\n[Action] Freeing {size} units at address {start}...")
        new_node = MyMemoryNode(start, size)

        # Put back in address order
        if not self.head or start < self.head.start:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next and curr.next.start < start:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

        # Merge if blocks are side by side
        self._merge_neighbors()

    def _merge_neighbors(self):
        curr = self.head
        while curr and curr.next:
            if curr.start + curr.length == curr.next.start:
                print(f"Merging blocks: {curr.start} and {curr.next.start}")
                curr.length += curr.next.length
                curr.next = curr.next.next
            else:
                curr = curr.next

    def print_status(self):
        print("Current Free List: ", end="")
        curr = self.head
        if not curr: print("FULL")
        while curr:
            print(f"[{curr.start}, len:{curr.length}]", end=" -> ")
            curr = curr.next
        print("END")
