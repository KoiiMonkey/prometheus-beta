import threading
import time
from typing import List

def sleep_sort(arr: List[int]) -> List[int]:
    """
    Implement the Sleep Sort algorithm.
    
    Sleep Sort is a sorting algorithm that uses threading and sleep times 
    to sort an array of positive integers. Each number creates a separate 
    thread that sleeps for a duration proportional to its value and then 
    adds itself to the result list.
    
    Args:
        arr (List[int]): A list of positive integers to be sorted.
    
    Returns:
        List[int]: A sorted list of input integers.
    
    Raises:
        ValueError: If any number in the input is negative.
    """
    # Validate input
    if not arr:
        return []
    
    # Check for negative numbers
    if any(num < 0 for num in arr):
        raise ValueError("Sleep sort only works with non-negative integers")
    
    # Create a thread-safe list to store results and synchronization primitives
    result = []
    lock = threading.Lock()
    start_event = threading.Event()
    threads_completed = []
    
    # Function to be run by each thread
    def sort_thread(num):
        # Wait for the start signal to synchronize threads
        start_event.wait()
        
        # Sleep proportional to the number's value
        time.sleep(num * 0.01)  # Increased delay for more consistent sorting
        
        # Thread-safe append to result list
        with lock:
            result.append(num)
            threads_completed.append(True)
    
    # Create threads for each number
    threads = []
    for num in arr:
        thread = threading.Thread(target=sort_thread, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Signal all threads to start simultaneously
    start_event.set()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Ensure all threads have completed before returning
    while len(threads_completed) < len(arr):
        time.sleep(0.001)
    
    return result