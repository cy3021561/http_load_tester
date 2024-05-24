import time
import threading
import requests
from http_load_tester.metrics import Metrics
from http_load_tester.report import generate_report

def load_test(url, qps, duration, headers=None, payload=None):
    """
    This function performs a load test on the given URL with the specified QPS (Queries Per Second) for a certain duration.

    :param url: The URL to perform the load test on
    :param qps: The number of requests to send per second
    :param duration: The duration of the load test in seconds
    """

    metrics = Metrics()  # Initializing Metrics object to store request metrics
    threads = []  # Initializing an empty list to store threads
    start_time = time.time()  # Getting the current time as the start time
    end_time = start_time + duration  # Calculating the end time by adding the duration to the start time
    interval = 1.0 / qps  # Calculating the interval between requests

    def worker(thread_id):
        """
        This function is the worker thread that sends requests at the specified QPS.

        :param thread_id: The ID of the current thread
        """
        next_request_time = start_time + thread_id * interval
        while next_request_time < end_time:
            current_time = time.time()
            if current_time < next_request_time:
                time.sleep(next_request_time - current_time)
            
            # Retry logic to the worker function to handle transient errors
            retry_count = 3
            while retry_count > 0:
                try:
                    response = requests.request("POST" if payload else "GET", url, headers=headers, json=payload)
                    latency = time.time() - next_request_time
                    metrics.record_request(latency, response.status_code)
                    print(f"Thread {thread_id}: Request completed with status {response.status_code}, latency {latency:.4f} seconds")
                    break  # Exit retry loop on success
                except requests.RequestException as e:
                    retry_count -= 1
                    if retry_count == 0:
                        metrics.record_error()
                        print(f"Thread {thread_id}: Request failed with error {e}")
            next_request_time += interval * qps

    for i in range(qps):  # Creating and starting threads
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:  # Waiting for all threads to complete
        thread.join()

    generate_report(metrics)  # Generating and displaying the load test report

# Example usage
if __name__ == "__main__":
    load_test("https://httpbin.org/get", 100, 5)  # Performing a load test on https://httpbin.org/get with 100 QPS for 5 seconds