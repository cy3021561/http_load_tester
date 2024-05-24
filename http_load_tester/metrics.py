import threading

class Metrics:
    def __init__(self):
        self.lock = threading.Lock() # Used to ensure that only one thread can access the shared variables at a time
        self.requests = 0
        self.errors = 0
        self.latencies = []

    # The record_request method is used to record the latency and status code of a request.
    def record_request(self, latency, status_code):
        try:
            with self.lock:
                self.requests += 1
                self.latencies.append(latency)
        except Exception as e:
            print(f"Error recording request: {e}")

    # The record_error method is used to record an error that occurred during a request.
    def record_error(self):
        try:
            with self.lock:
                self.errors += 1
                self.requests += 1
        except Exception as e:
            print(f"Error recording error: {e}")

    # The get_summary method is used to calculate and return a summary of the metrics.
    def get_summary(self):
        with self.lock:
            total_requests = self.requests
            error_rate = self.errors / total_requests if total_requests > 0 else 0
            avg_latency = sum(self.latencies) / len(self.latencies) if self.latencies else 0
            return {
                'total_requests': total_requests,
                'errors': self.errors,
                'error_rate': error_rate,
                'average_latency': avg_latency,
                'latencies': self.latencies,
            }