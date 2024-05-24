import unittest
from http_load_tester.metrics import Metrics

class TestMetrics(unittest.TestCase):
    def test_metrics_recording(self):
        metrics = Metrics()

        # Define test cases
        metrics.record_request(0.1, 200)
        metrics.record_request(0.2, 200)
        metrics.record_error()

        # Get the summary of the metrics
        summary = metrics.get_summary()

        # Check results
        self.assertEqual(summary['total_requests'], 3)
        self.assertEqual(summary['errors'], 1)
        self.assertAlmostEqual(summary['average_latency'], 0.15)


if __name__ == '__main__':
    unittest.main()