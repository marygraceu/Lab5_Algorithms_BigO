# APPENDIX 2: University Enrollment Records
# Student: PENA - TUPM-26-1140

LAST_NAME = "PENA"
STUDENT_ID = "TUPM-26-1140"
FAVORITE_ARTIST = "LANY"

NAME_LENGTH = len(LAST_NAME) # 4
ID_SUM = 14
SEED_DIGIT = 4
ARTIST_LENGTH = len(FAVORITE_ARTIST) # 4

print(f"STUDENT: {LAST_NAME}, ID: {STUDENT_ID}")
print(f"SEED_DIGIT={SEED_DIGIT}, ID_SUM={ID_SUM}, NAME_LENGTH={NAME_LENGTH}, ARTIST_LENGTH={ARTIST_LENGTH}\n")

# Requirement 1: Generate two sorted enrollment datasets
def generate_dataset_a():
    n = SEED_DIGIT + 5
    step = SEED_DIGIT + 1
    return [ID_SUM + (i * step) for i in range(n)]

def generate_dataset_b():
    n = NAME_LENGTH + 5
    base = ARTIST_LENGTH * 10
    step = NAME_LENGTH + 1
    return [base + (i * step) for i in range(n)]

Dataset_A = generate_dataset_a()
Dataset_B = generate_dataset_b()

# Requirement 2 & 3: Consolidate and count comparisons
def merge_sorted(a, b):
    i = j = 0
    consolidated = []
    comparisons = 0
    while i < len(a) and j < len(b):
        comparisons += 1
        if a[i] <= b[j]:
            consolidated.append(a[i])
            i += 1
        else:
            consolidated.append(b[j])
            j += 1
    consolidated.extend(a[i:])
    consolidated.extend(b[j:])
    return consolidated, comparisons

Consolidated, comp_count = merge_sorted(Dataset_A, Dataset_B)

# Requirement 4: Verify final order
is_sorted = all(Consolidated[k] <= Consolidated[k+1] for k in range(len(Consolidated)-1))

# Assessment Data
print("========== ASSESSMENT DATA ==========")
print(f"Department A dataset: {Dataset_A}")
print(f"Department B dataset: {Dataset_B}")
print(f"Consolidated dataset: {Consolidated}")
print(f"Number of records before: Dept A={len(Dataset_A)}, Dept B={len(Dataset_B)}, Total={len(Dataset_A)+len(Dataset_B)}")
print(f"Number of records after consolidation: {len(Consolidated)}")
print(f"Comparison count: {comp_count}")
print(f"Ordering verification: {'Verified - Ascending order' if is_sorted else 'Failed'}")
print(f"Time and space complexity: Time O(n+m), Space O(n+m)")
print(f"Final Output: {Consolidated}")