def running_average():
    """
    Coroutine generator to maintain a running average.
    - Receives numbers via .send()
    - Yields current average after each number
    """
    total = 0
    count = 0
    average = None
    while True:
        # Yield current average and wait for the next number
        num = yield average
        if num is None:
            continue  
        total += num
        count += 1
        average = total / count

if __name__ == "__main__":
    # Create the generator
    avg_gen = running_average()

    # Prime the generator (run up to first yield)
    print(next(avg_gen))  # Initially yields None

    # Send numbers and print running average
    print(avg_gen.send(10))  # Output: 10.0
    print(avg_gen.send(20))  # Output: 15.0
    print(avg_gen.send(30))  # Output: 20.0
    print(avg_gen.send(40))  # Output: 25.0
    print(avg_gen.send(50))  # Output: 30.0