import sys
from typing import List, Dict, Any, Generator

def batch_generator(records: List[Dict[str, Any]], batch_size: int = 5) -> Generator[List[Dict[str, Any]], None, None]:
    """
    A generator that yields batches of records from an input list.
    """
    if not isinstance(records, list):
        raise TypeError("Records must be a list.")
    if not isinstance(batch_size, int) or batch_size <= 0:
        raise ValueError("Batch size must be a positive integer.")
    num_records = len(records)
    for i in range(0, num_records, batch_size):
        yield records[i : i + batch_size]


def simulate_validation(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Placeholder for actual validation. Returns the record marked as SIMULATED_VALID.
    """
    return {**record, "status": "SIMULATED_VALID"}


if __name__ == "__main__":
    NUM_RECORDS = 10_000
    print(f"Generating {NUM_RECORDS} mock records...")
    large_dataset = [
        {"email": f"student{i}@univ.edu", "id": f"{i:09d}", "password": f"Password{i}"}
        for i in range(NUM_RECORDS)
    ]
    print(f"Finished generating {NUM_RECORDS} mock records.")
    print("\n--- Memory Usage Comparison ---")
    list_memory = sys.getsizeof(large_dataset) / 1024  # KB
    print(f"Memory usage of full list ({NUM_RECORDS} records): {list_memory:.2f} KB")
    generator_instance = batch_generator(large_dataset, batch_size=100)
    generator_memory = sys.getsizeof(generator_instance) / 1024  # KB
    print(f"Memory usage of generator object (initially): {generator_memory:.2f} KB")
    print("\n--- Streaming Records with Generator and Validation ---")
    processed_count = 0
    max_batch_size = 100
    memory_usage_during_processing = []
    print("Simulating streaming validation...")
    for batch_num, batch in enumerate(batch_generator(large_dataset, batch_size=max_batch_size)):
        current_batch_memory = sys.getsizeof(batch) / 1024
        memory_usage_during_processing.append(current_batch_memory)
        validated_batch = [simulate_validation(record) for record in batch]
        processed_count += len(validated_batch)
        if (batch_num + 1) % 100 == 0:
            print(f"  Processed {processed_count} records. Current batch memory: {current_batch_memory:.2f} KB")
    if memory_usage_during_processing:
        max_batch_memory = max(memory_usage_during_processing)
        print(f"\nValidated {processed_count} records.")
        print(f"Max memory used for a single batch during streaming: {max_batch_memory:.2f} KB")
        print(f"Generator object memory: {generator_memory:.2f} KB")
    else:
        print("No records processed (dataset might be empty).")
