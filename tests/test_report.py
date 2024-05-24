import unittest
from http_load_tester.metrics import Metrics
from http_load_tester.report import generate_report

class TestReport(unittest.TestCase):
    def test_generate_report(self):
        # Create a new Metrics object to record request metrics
        metrics = Metrics()
        
        # Record three requests with response times and status codes
        metrics.record_request(0.1, 200)
        metrics.record_request(0.2, 200)
        metrics.record_error()
        
        # Generate a report based on the recorded metrics
        generate_report(metrics)
        
        # Here we could redirect stdout to a string and verify the output

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()