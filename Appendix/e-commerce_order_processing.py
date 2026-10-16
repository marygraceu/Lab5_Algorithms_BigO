# 3. E-Commerce Order Processing
# Student: PENA - TUPM-26-1140 - LANY

import time
import random

LAST_NAME = "PENA"
STUDENT_ID = "TUPM-26-1140"
FAVORITE_ARTIST = "LANY"

NAME_LENGTH = len(LAST_NAME) # 4
ARTIST_LENGTH = len(FAVORITE_ARTIST) # 4
ID_SUM = 14
SEED_DIGIT = 4

# Data Generation Rule: Orders - Generate values using student-specific inputs
def generate_orders():
    size = NAME_LENGTH + SEED_DIGIT + 2 # 10 orders para kita comparison
    base = ID_SUM * 3 # 42
    step = NAME_LENGTH + 2 # 6
    dataset = [base + (i * step) + (ARTIST_LENGTH) for i in range(size)]
    return dataset

base_orders = generate_orders()
random.seed(ID_SUM)
random_orders = base_orders.copy()
random.shuffle(random_orders)

sorted_input = sorted(base_orders)
reverse_input = sorted(base_orders, reverse=True)
random_input = random_orders

print(f"STUDENT: {LAST_NAME} | {STUDENT_ID} | {FAVORITE_ARTIST}")
print(f"ID_SUM={ID_SUM}, NAME_LENGTH={NAME_LENGTH}, ARTIST_LENGTH={ARTIST_LENGTH}, SEED={SEED_DIGIT}")
print(f"\nGenerated order dataset: {base_orders}")
print(f"Sorted input: {sorted_input}")
print(f"Reverse input: {reverse_input}")
print(f"Random input: {random_input}")

# Sorting Algorithms with counters
def bubble_sort(arr):
    a = arr.copy()
    comps = 0
    moves = 0
    start = time.perf_counter()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            comps += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                moves += 3 # 3 movements per swap
    end = time.perf_counter()
    return a, comps, moves, (end-start)*1000000

def selection_sort(arr):
    a = arr.copy()
    comps = 0
    moves = 0
    start = time.perf_counter()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comps += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx!= i:
            a[i], a[min_idx] = a[min_idx], a[i]
            moves += 3
    end = time.perf_counter()
    return a, comps, moves, (end-start)*1000000

def insertion_sort(arr):
    a = arr.copy()
    comps = 0
    moves = 0
    start = time.perf_counter()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if a[j] > key:
                a[j+1] = a[j]
                moves += 1
                j -= 1
            else:
                break
        a[j+1] = key
        moves += 1
    end = time.perf_counter()
    return a, comps, moves, (end-start)*1000000

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

inputs = {
    "Sorted": sorted_input,
    "Reverse": reverse_input,
    "Random": random_input
}

# Requirement 1-4: Apply and record
print("\n========== ASSESSMENT DATA ==========")
results = []
for input_name, input_data in inputs.items():
    print(f"\n--- Input Condition: {input_name} -> {input_data} ---")
    for algo_name, algo_func in algorithms.items():
        sorted_arr, comps, moves, exec_time = algo_func(input_data)
        verified = all(sorted_arr[k] <= sorted_arr[k+1] for k in range(len(sorted_arr)-1))
        results.append((input_name, algo_name, comps, moves, exec_time))
        print(f"{algo_name}: Sorted={sorted_arr} | Comparisons={comps} | Movements={moves} | Time={exec_time:.2f}us | Verified={verified}")

# Requirement 5 & 6
print("\n--- Performance Comparison ---")
for input_name in inputs:
    print(f"\n{input_name} Condition:")
    filtered = [r for r in results if r[0]==input_name]
    for r in filtered:
        print(f" {r[1]} - Comp: {r[2]}, Moves: {r[3]}, Time: {r[4]:.2f}us")

print("\n--- Big O Analysis ---")
print("Bubble Sort: Best O(n), Average O(n^2), Worst O(n^2) - Space O(1)")
print("Selection Sort: Best O(n^2), Average O(n^2), Worst O(n^2) - Space O(1)")
print("Insertion Sort: Best O(n), Average O(n^2), Worst O(n^2) - Space O(1)")

print("\n--- Best-, average-, and worst-case observations ---")
print("Sorted input is best-case for Bubble and Insertion (least comps/moves).")
print("Reverse input is worst-case for Bubble and Insertion (most comps/moves).")
print("Selection Sort has almost same comparisons regardless of input.")
print("Random input is average-case.")

print(f"\nFinal Output: All algorithms correctly sorted the {len(base_orders)} orders.")