import time

def load_test(function, times):
    start_time = time.time()
    for _ in range(times):
        function()
    end_time = time.time()
    print(f"Time taken for {times} executions: {end_time - start_time} seconds")

def stress_test(function, times, concurrent_users):
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=concurrent_users) as executor:
        futures = [executor.submit(function) for _ in range(times)]
        for future in futures:
            future.result()
    print(f"Completed stress test with {concurrent_users} concurrent users")