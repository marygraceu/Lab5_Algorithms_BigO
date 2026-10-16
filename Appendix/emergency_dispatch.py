# APPENDIX NO. 1
# Emergency Dispatch Record Search

LAST_NAME = "Pena"
STUDENT_ID = "TUPM-26-1140"
FAVORITE_ARTIST = "LANY"
RECORD_COUNT = 10


def sum_digits(student_id):
    """Add all numeric digits in the student ID."""
    return sum(int(char) for char in student_id if char.isdigit())


def alphabet_sum(text):
    """Calculate letter values using A=1, B=2, ..., Z=26."""
    return sum(ord(char.upper()) - ord("A") + 1
               for char in text if char.isalpha())


def linear_search(records, target):
    """Return the target index and the number of comparisons."""
    comparisons = 0
    for index, record in enumerate(records):
        comparisons += 1
        if record == target:
            return index, comparisons
    return -1, comparisons


def main():
    seed_digit = int(STUDENT_ID[-1])
    id_sum = sum_digits(STUDENT_ID)
    name_length = len(LAST_NAME)
    artist_length = len(FAVORITE_ARTIST)
    artist_sum = alphabet_sum(FAVORITE_ARTIST)

    # Clearly defined formula for generating reproducible incident IDs.
    start_value = (seed_digit * 100) + id_sum + artist_sum
    interval = name_length + artist_length
    original_records = [
        start_value + (i * interval) for i in range(RECORD_COUNT)
    ]

    # Select a target deterministically from the generated records.
    target_index = (id_sum + artist_sum) % RECORD_COUNT
    target_incident = original_records[target_index]

    # Rotate left by SEED_DIGIT positions.
    rotation_point = seed_digit % len(original_records)
    rotated_records = (
        original_records[rotation_point:]
        + original_records[:rotation_point]
    )

    # Search target in both lists and count actual comparisons.
    original_index, original_comparisons = linear_search(
        original_records, target_incident
    )
    rotated_index, rotated_comparisons = linear_search(
        rotated_records, target_incident
    )

    print("=" * 52)
    print("APPENDIX NO. 1: EMERGENCY DISPATCH RECORD SEARCH")
    print("=" * 52)

    print("\nASSESSMENT DATA: STUDENT-SPECIFIC INPUTS")
    print(f"LAST_NAME: {LAST_NAME}")
    print(f"STUDENT_ID: {STUDENT_ID}")
    print(f"FAVORITE_ARTIST: {FAVORITE_ARTIST}")
    print(f"SEED_DIGIT: {seed_digit}")
    print(f"ID_SUM: {id_sum}")
    print(f"NAME_LENGTH: {name_length}")
    print(f"ARTIST_LENGTH: {artist_length}")
    print(f"ARTIST_SUM: {artist_sum}")

    print("\nDATA GENERATION RULE")
    print("start_value = SEED_DIGIT * 100 + ID_SUM + ARTIST_SUM")
    print("interval = NAME_LENGTH + ARTIST_LENGTH")
    print(f"start_value = {start_value}")
    print(f"interval = {interval}")

    print("\nORIGINAL DATASET")
    print(original_records)

    print("\nROTATION DETAILS")
    print(f"Rotation point: {rotation_point}")
    print("Rotation direction: left")
    print("\nROTATED DATASET")
    print(rotated_records)

    print("\nTARGET INCIDENT")
    print(f"Target incident ID: {target_incident}")

    print("\nSEARCH RESULTS")
    print("Linear Search on Original Dataset")
    if original_index >= 0:
        print(f"Status: Found at index {original_index} "
              f"(position {original_index + 1})")
    else:
        print("Status: Not Found")
    print(f"Comparisons: {original_comparisons}")

    print("\nLinear Search on Rotated Dataset")
    if rotated_index >= 0:
        print(f"Status: Found at index {rotated_index} "
              f"(position {rotated_index + 1})")
    else:
        print("Status: Not Found")
    print(f"Comparisons: {rotated_comparisons}")

    print("\nCOMPARISON SUMMARY")
    print(f"Original dataset comparisons: {original_comparisons}")
    print(f"Rotated dataset comparisons: {rotated_comparisons}")
    print("Comparison-count difference: "
          f"{abs(original_comparisons - rotated_comparisons)}")

    print("\nVERIFICATION")
    print(f"Original record count: {len(original_records)}")
    print(f"Rotated record count: {len(rotated_records)}")
    print(f"All records preserved: "
          f"{sorted(original_records) == sorted(rotated_records)}")
    print(f"Original dataset sorted: "
          f"{original_records == sorted(original_records)}")
    print(f"Rotated dataset sorted: "
          f"{rotated_records == sorted(rotated_records)}")

    print("\nTIME AND SPACE COMPLEXITY")
    print("Linear Search: best O(1), average/worst O(n) time.")
    print("Linear Search auxiliary space: O(1).")
    print("Generating records: O(n) time and O(n) space.")
    print("Rotating records: O(n) time and O(n) additional space.")

    print("\nFINAL OUTPUT")
    print("The target incident was searched in the original and rotated datasets.")
    print("Actual search positions and comparison counts are reported above.")
    print("The formula used for generating incident IDs is shown above.")


if __name__ == "__main__":
    main()